use std::{
    collections::{HashMap, HashSet},
    fmt::{self, Display},
};

use crate::{
    cached_lambda,
    py_types::{ExtraPySelfOps, Tensor, PY_SCALAR_TO_TENSOR, TENSOR_SCALE},
    pycall,
    tensor_util::{Shape, TorchDeviceDtype},
};

use super::{
    circuit_optimizer::OptimizationSettings,
    circuit_utils::{hash_to_node, toposort_circuit},
    get_compatible_dtype,
    prelude::*,
    print::oom_fmt,
    scheduling_z3::schedule_dag_strategy_ints,
    visit_circuit, ArrayConstant, HashBytes, ScalarConstant, Symbol,
};
use crate::pyo3_prelude::*;
use crate::util::filter_to_idx;
use num_bigint::BigUint;
use pyo3::{create_exception, exceptions::PyException};
use thiserror::Error;

#[derive(Clone, Debug)]
pub enum Instruction {
    Drop(HashBytes),
    Compute(CircuitRc),
}

// impl IntoPy<PyObject> for Instruction {
//     fn into_py(self, py: Python<'_>) -> PyObject {
//         ().into_py(py)
//     }
// }

#[derive(Clone, Debug)]
pub struct Schedule {
    instructions: Vec<Instruction>,
    constants: HashMap<HashBytes, Tensor>,
    // keep scalar constants seperate so adjust numerical scale can work without losing precision
    // before when these were in tensors, they had to be right dtype and therefore overflowed when
    // adjustment needed
    scalar_constants: HashMap<HashBytes, ScalarConstant>,
    device_dtype: TorchDeviceDtype,
}
impl Schedule {
    pub fn get_stats(&self) -> ScheduleStats {
        let mut mem: BigUint = BigUint::from(0usize);
        let mut max_mem: BigUint = BigUint::from(0usize);
        let mut biggest: HashMap<HashBytes, CircuitRc> = HashMap::new();
        let mut current: HashMap<HashBytes, CircuitRc> = HashMap::new();
        for instruction in self.instructions.clone() {
            match instruction {
                Instruction::Drop(drop) => {
                    let dropped = current.remove(&drop).unwrap();
                    mem -= dropped.info().numel();
                }
                Instruction::Compute(c) => {
                    current.insert(c.info().hash, c.clone());
                    mem += c.info().numel();
                    if mem > max_mem {
                        max_mem = mem.clone();
                        biggest = current.clone();
                    }
                }
            }
        }
        ScheduleStats {
            max_mem,
            constant_mem: self
                .constants
                .iter()
                .map(|(_h, t)| t.shape().iter().product::<usize>())
                .sum(),
            max_circuit_set: biggest.values().cloned().collect(),
        }
    }
}

#[derive(Clone, Debug)]
pub struct ScheduleStats {
    max_mem: BigUint,
    constant_mem: BigUint, // this has already been allocated so it can't be over 2^64
    max_circuit_set: HashSet<CircuitRc>,
}

#[derive(Error, Debug)]
pub enum SchedulingError {
    #[error("{string}")]
    CannotFitInMemory {
        max_memory: usize,
        memory_chunks: usize,
        node_memories: Vec<usize>,
        string: String,
    },
}

create_exception!(
    rust_circuit,
    PyOOMError,
    PyException,
    "OOM error from compiler"
);

impl From<SchedulingError> for PyErr {
    fn from(err: SchedulingError) -> Self {
        PyErr::new::<PyOOMError, _>(format!("error (TODO: better) {}", err))
    }
}

impl Display for ScheduleStats {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut shapes = self
            .max_circuit_set
            .iter()
            .map(|x| x.info().shape.clone())
            .collect::<Vec<Shape>>();
        shapes.sort_by_key(|x| std::cmp::Reverse(x.iter().product::<usize>()));
        let shapes_and_percents: String = shapes
            .iter()
            .map(|x| {
                format!(
                    "{:?} {}%",
                    x,
                    // biguint doesn't have cast f64? that would be less lossy than truncate
                    (x.iter().product::<usize>() as f64 / self.max_mem.to_u64_digits()[0] as f64
                        * 100.0) as i64
                )
            })
            .collect::<Vec<String>>()
            .join(", ");
        let result = format!(
            "ScheduleStats: max: {} const: {} shapes: {}",
            oom_fmt(self.max_mem.clone()),
            oom_fmt(self.constant_mem.clone()),
            shapes_and_percents
        );
        write!(f, "{}", result)
    }
}

pub fn evaluate_schedule(schedule: Schedule) -> HashMap<HashBytes, Tensor> {
    let mut live: HashMap<HashBytes, Tensor> = schedule.constants.clone();
    live.extend(
        schedule
            .scalar_constants
            .iter()
            .map(|x| (*x.0, x.1.eval_tensors(&[], &schedule.device_dtype).unwrap())),
    );
    for s in &schedule.instructions {
        match s {
            Instruction::Compute(circ) => {
                circ.children().for_each(|x: CircuitRc| {
                    if !live.contains_key(&x.info().hash) {
                        println!("FAIL");
                        dbg!(schedule
                            .instructions
                            .iter()
                            .filter_map(|ins| {
                                match ins {
                                    Instruction::Drop(d) => {
                                        if *d == x.info().hash {
                                            Some(ins)
                                        } else {
                                            None
                                        }
                                    }
                                    Instruction::Compute(c) => {
                                        if c == &x {
                                            Some(ins)
                                        } else {
                                            None
                                        }
                                    }
                                }
                            })
                            .collect::<Vec<&Instruction>>());
                        circ.compiler_print();
                        x.compiler_print();
                        panic!();
                    }
                });
                let tensors: Vec<Tensor> = circ
                    .children()
                    .map(|x| live[&x.info().hash].clone())
                    .collect();
                let result_err = circ.eval_tensors(&tensors, &schedule.device_dtype);
                if result_err.is_err() {
                    println!("errored evaluate");
                    circ.compiler_print()
                }
                let result = result_err.unwrap();
                assert!(result.shape()[..] == circ.info().shape[..]);
                live.insert(circ.info().hash, result);
            }
            Instruction::Drop(hash) => {
                live.remove(hash);
            }
        }
    }
    live
}

pub fn evaluate_schedule_adjust_numerical_scale(
    schedule: Schedule,
    settings: OptimizationSettings,
) -> HashMap<HashBytes, Tensor> {
    // we store (tensor, scale) where scale is a number the tensor's been multiplied by
    // so (tensor(1e10),1.0) evaluates to same as (tensor(1),1e-10)
    let mul = |tup: &(Tensor, f64), m: f64| -> (Tensor, f64) {
        Python::with_gil(|py| (tup.0.clone().py_mul(py, m).unwrap(), tup.1 * m))
    };
    let set_scale = |tup: &(Tensor, f64), new_scale: f64| -> (Tensor, f64) {
        Python::with_gil(|py| {
            (
                tup.0.clone().py_mul(py, new_scale / tup.1).unwrap(),
                new_scale,
            )
        })
    };
    let clamp = |tup: &(Tensor, f64)| -> (Tensor, f64) {
        let tensor_scale: f64 = Python::with_gil(|py| {
            TENSOR_SCALE
                .call(py, (tup.0.clone(),), None)
                .unwrap()
                .extract(py)
                .unwrap()
        });
        if tensor_scale > settings.numerical_scale_max
            || tensor_scale < settings.numerical_scale_min
        {
            mul(tup, 1.0 / tensor_scale)
        } else {
            tup.clone()
        }
    };
    let uniformize = |tups: &Vec<(Tensor, f64)>| -> Vec<(Tensor, f64)> {
        if tups.is_empty() || tups.iter().all(|x| x.1 == tups[0].1) {
            tups.clone()
        } else {
            let new_scale: f64 = tups
                .iter()
                .map(|x| x.1)
                .reduce(|a, b| if a > b { a } else { b })
                .unwrap();
            tups.iter().map(|x| set_scale(x, new_scale)).collect()
        }
    };

    let mut live: HashMap<HashBytes, (Tensor, f64)> = schedule
        .constants
        .iter()
        .map(|x| (*x.0, clamp(&(x.1.clone(), 1.0))))
        .collect();
    live.extend(schedule.scalar_constants.iter().map(|(h, s)| {
        (*h, {
            let value_scale = s.value.abs();
            if value_scale > settings.numerical_scale_max
                || value_scale < settings.numerical_scale_min && value_scale != 0.0
            {
                (
                    pycall!(
                        PY_SCALAR_TO_TENSOR,
                        (
                            s.value.signum(),
                            s.info().shape.clone(),
                            schedule.device_dtype.clone(),
                        )
                    ),
                    1.0 / value_scale,
                )
            } else {
                (
                    pycall!(
                        PY_SCALAR_TO_TENSOR,
                        (
                            s.value,
                            s.info().shape.clone(),
                            schedule.device_dtype.clone(),
                        )
                    ),
                    1.0,
                )
            }
        })
    }));
    for s in &schedule.instructions {
        match s {
            Instruction::Compute(circ) => {
                circ.children().for_each(|x: CircuitRc| {
                    if !live.contains_key(&x.info().hash) {
                        println!("FAIL");
                        dbg!(schedule
                            .instructions
                            .iter()
                            .filter_map(|ins| {
                                match ins {
                                    Instruction::Drop(d) => {
                                        if *d == x.info().hash {
                                            Some(ins)
                                        } else {
                                            None
                                        }
                                    }
                                    Instruction::Compute(c) => {
                                        if c == &x {
                                            Some(ins)
                                        } else {
                                            None
                                        }
                                    }
                                }
                            })
                            .collect::<Vec<&Instruction>>());
                        circ.compiler_print();
                        x.compiler_print();
                        panic!();
                    }
                });
                let tensors_and_scales: Vec<(Tensor, f64)> = circ
                    .children()
                    .map(|x| live[&x.info().hash].clone())
                    .collect();
                let tensors: Vec<Tensor> = tensors_and_scales.iter().map(|x| x.0.clone()).collect();
                let result = match &***circ {
                    Circuit::Einsum(_) => {
                        let new_scale = tensors_and_scales.iter().map(|x| x.1).product();
                        clamp(&(
                            circ.eval_tensors(&tensors, &schedule.device_dtype).unwrap(),
                            new_scale,
                        ))
                    }
                    Circuit::Add(_) | Circuit::Concat(_) => {
                        let new_ts = uniformize(&tensors_and_scales);
                        (
                            circ.eval_tensors(
                                &new_ts.iter().map(|x| x.0.clone()).collect::<Vec<_>>(),
                                &schedule.device_dtype,
                            )
                            .unwrap(),
                            new_ts[0].1,
                        )
                    }
                    Circuit::GeneralFunction(_) => {
                        let new_ts: Vec<(Tensor, f64)> = tensors_and_scales
                            .iter()
                            .map(|x| set_scale(x, 1.0))
                            .collect();
                        clamp(&(
                            circ.eval_tensors(
                                &new_ts.iter().map(|x| x.0.clone()).collect::<Vec<_>>(),
                                &schedule.device_dtype,
                            )
                            .unwrap(),
                            1.0,
                        ))
                    }
                    Circuit::Index(_) | Circuit::Rearrange(_) | Circuit::Scatter(_) => (
                        circ.eval_tensors(
                            &tensors_and_scales
                                .iter()
                                .map(|x| x.0.clone())
                                .collect::<Vec<_>>(),
                            &schedule.device_dtype,
                        )
                        .unwrap(),
                        tensors_and_scales[0].1,
                    ),
                    _ => {
                        unimplemented!()
                    }
                };
                assert!(result.0.shape()[..] == circ.info().shape[..]);
                live.insert(circ.info().hash, result);
            }
            Instruction::Drop(hash) => {
                live.remove(hash);
            }
        }
    }
    live.iter()
        .map(|(k, v)| (*k, set_scale(v, 1.0).0))
        .collect()
}

/// this supports dropping and recomputing. if you have an Evaluate(CircuitRc) of something you already evaluated
/// it's assumed you dropped this and are recomputing it
pub fn order_to_schedule(
    order: &Vec<CircuitRc>,
    constants: &Vec<ArrayConstant>,
    scalar_constants: &Vec<ScalarConstant>,
    to_keep: HashSet<HashBytes>,
    device_dtype: TorchDeviceDtype,
) -> Schedule {
    let mut result: Schedule = Schedule {
        instructions: vec![],
        constants: constants
            .iter()
            .map(|x| (x.info().hash, x.value.clone()))
            .collect(),
        scalar_constants: scalar_constants
            .iter()
            .map(|x| (x.info().hash, x.clone()))
            .collect(),
        device_dtype,
    };

    let mut seen_dependencies: HashSet<HashBytes> = HashSet::new();
    for ex in order.iter().rev() {
        for child in ex.children() {
            let dep = child.info().hash;
            if !matches!(
                &**child,
                Circuit::ArrayConstant(_) | Circuit::ScalarConstant(_)
            ) && seen_dependencies.insert(dep)
                && !to_keep.contains(&dep)
            {
                result.instructions.push(Instruction::Drop(dep));
            }
        }
        result.instructions.push(Instruction::Compute(ex.clone()));
        // seen_dependencies.remove(&ex.info().hash);
    }
    result.instructions.reverse();
    result
}

#[pyclass]
#[derive(Default, Clone, Debug)]
pub struct Dag {
    pub children: Vec<Vec<usize>>,
    pub parents: Vec<Vec<usize>>,
    pub node_costs: Vec<usize>,
    pub node_hashes: Vec<HashBytes>,
    pub hash_to_node: HashMap<HashBytes, usize>,
}
impl Dag {
    pub fn get_outputs(&self) -> Vec<usize> {
        filter_to_idx(&self.parents.iter().collect(), &mut |y| y.is_empty())
    }
}

pub fn circuits_to_dag(circuits: &[&Circuit]) -> Dag {
    let mut result: Dag = Default::default();
    let number_node = |c: &Circuit, result: &mut Dag| -> usize {
        if let Some(idx) = result.hash_to_node.get(&c.info().hash) {
            return *idx;
        }
        result
            .node_costs
            .push(if !matches!(c, Circuit::ArrayConstant(_)) {
                assert!(c.info().numel() < BigUint::from(usize::MAX));
                c.info().numel().to_u64_digits()[0] as usize
            } else {
                0
            });
        result.node_hashes.push(c.info().hash);
        result
            .hash_to_node
            .insert(c.info().hash, result.node_hashes.len() - 1);
        result.children.push(vec![]);
        result.parents.push(vec![]);
        result.node_hashes.len() - 1
    };
    for circuit in circuits {
        visit_circuit(circuit, &mut |c: &Circuit| {
            if !matches!(c, Circuit::ArrayConstant(_) | Circuit::ScalarConstant(_)) {
                let my_number = number_node(c, &mut result);
                let children_to_consider: Vec<CircuitRc> = c
                    .children()
                    .filter(|child| {
                        !matches!(
                            &***child,
                            Circuit::ArrayConstant(_) | Circuit::ScalarConstant(_)
                        )
                    })
                    .collect();
                result.children[my_number] = children_to_consider
                    .iter()
                    .map(|child| number_node(child, &mut result))
                    .collect();
                for child in children_to_consider {
                    let new_num = number_node(&child, &mut result);
                    result.parents[new_num].push(my_number);
                }
            }
        });
    }
    result
}

fn simplify_dag_kept_nodes(dag: &Dag, chunk_size: usize) -> Vec<usize> {
    (0..dag.node_costs.len())
        .filter(|i| dag.node_costs[*i] >= chunk_size)
        .collect()
}

fn simplify_dag_for_scheduling_and_kept_nodes(dag: &Dag, chunk_size: usize) -> (Dag, Vec<usize>) {
    let nodes_to_keep: Vec<usize> = simplify_dag_kept_nodes(dag, chunk_size);
    let old_to_new: HashMap<usize, usize> = nodes_to_keep
        .iter()
        .enumerate()
        .map(|x| (*x.1, x.0))
        .collect();
    let mut result = Dag {
        node_hashes: nodes_to_keep.iter().map(|x| dag.node_hashes[*x]).collect(),
        hash_to_node: nodes_to_keep
            .iter()
            .enumerate()
            .map(|(i, x)| (dag.node_hashes[*x], i))
            .collect(),
        node_costs: nodes_to_keep.iter().map(|x| dag.node_costs[*x]).collect(),
        children: vec![vec![]; nodes_to_keep.len()],
        parents: vec![vec![]; nodes_to_keep.len()],
    };

    cached_lambda! {
        let mut important_children = |old_i:usize|->Vec<usize> = {
            let old_children = &dag.children[old_i];
            old_children.iter().flat_map(|old_child|{
                if let Some(n)=old_to_new.get(old_child){
                    vec![*n]
                }else{
                    important_children(*old_child)
                }
            }).collect()
        };
    }

    for (new_i, old_i) in nodes_to_keep.iter().enumerate() {
        let children = important_children(*old_i);
        result.children[new_i] = children.clone();
        for child in children {
            result.parents[child].push(new_i);
        }
    }

    (result, nodes_to_keep)
}

fn subset_order_to_full_order(
    order: &Vec<usize>,
    kept_nodes: &Vec<usize>,
    dag: &Dag,
) -> Vec<usize> {
    let mut result: Vec<usize> = vec![];
    let mut result_set: HashSet<usize> = HashSet::new();

    fn recurse(orig_i: usize, result: &mut Vec<usize>, result_set: &mut HashSet<usize>, dag: &Dag) {
        if !result_set.contains(&orig_i) {
            for child in &dag.children[orig_i] {
                if !result_set.contains(child) {
                    recurse(*child, result, result_set, dag);
                }
            }
            result.push(orig_i);
            result_set.insert(orig_i);
        }
    }

    for sub_i in order {
        let orig_i = kept_nodes[*sub_i];
        recurse(orig_i, &mut result, &mut result_set, dag)
    }
    for output in dag.get_outputs() {
        recurse(output, &mut result, &mut result_set, dag);
    }

    result
}

pub fn circuit_to_schedule(
    circuit: CircuitRc,
    settings: OptimizationSettings,
) -> Result<Schedule, SchedulingError> {
    let max_elements_in_memory = settings.max_memory / get_compatible_dtype(&circuit).size();
    let chunk_size = max_elements_in_memory / settings.scheduling_num_mem_chunks;
    let dag = circuits_to_dag(&[&**circuit]);

    let order_result = {
        // currently dag simplifications increase achievable memory usage unfortunately
        // todo make better simplifications
        if settings.scheduling_simplify {
            // operate on subset dag
            let (sub_dag, kept_nodes) =
                simplify_dag_for_scheduling_and_kept_nodes(&dag, chunk_size);
            if settings.verbose >= 2 {
                println!(
                    "dag sizes: orig: {} pruned: {}",
                    dag.node_costs.len(),
                    sub_dag.node_costs.len()
                );
            }
            schedule_dag_strategy_ints(
                &sub_dag,
                settings.verbose,
                max_elements_in_memory,
                settings.scheduling_num_mem_chunks,
            )
            .map(|sub_order| subset_order_to_full_order(&sub_order, &kept_nodes, &dag))
        } else {
            schedule_dag_strategy_ints(
                &dag,
                settings.verbose,
                max_elements_in_memory,
                settings.scheduling_num_mem_chunks,
            )
        }
    };
    if order_result.is_err() {
        circuit.compiler_print();
    }

    let order = order_result?;

    let to_node = hash_to_node(&circuit);
    let circuit_order: Vec<CircuitRc> = order
        .iter()
        .map(|x| to_node[&dag.node_hashes[*x]].clone())
        .collect();
    let out = order_to_schedule(
        &circuit_order,
        &to_node
            .iter()
            .filter_map(|x| x.1.as_array_constant().cloned())
            .collect(),
        &to_node
            .iter()
            .filter_map(|x| x.1.as_scalar_constant().cloned())
            .collect(),
        dag.get_outputs()
            .iter()
            .map(|x| dag.node_hashes[*x])
            .collect(),
        get_compatible_dtype(&circuit),
    );

    Ok(out)
}

pub fn circuit_to_schedule_naive_toposort(circuit: CircuitRc) -> Schedule {
    let toposorted = toposort_circuit(circuit.clone());
    order_to_schedule(
        &toposorted,
        &vec![],
        &vec![],
        HashSet::from([circuit.info().hash]),
        get_compatible_dtype(&circuit),
    )
}

#[pyfunction]
pub fn scheduled_evaluate(
    circuit: CircuitRc,
    settings: OptimizationSettings,
) -> Result<Tensor, SchedulingError> {
    let schedule = circuit_to_schedule(circuit.clone(), settings)?;
    Ok(evaluate_schedule(schedule)[&circuit.info().hash].clone())
}
