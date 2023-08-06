use crate::{circuit::print::rust_expression_notation_circuit, pyo3_prelude::*};

use super::{
    algebraic_rewrite::deep_optimize_einsums,
    canonicalize::deep_canonicalize,
    compiler_heuristics::deep_maybe_distribute,
    compiler_strip::strip_names,
    deep_rewrite::deep_heuristic_nest_adds,
    deep_rewrite::{compiler_simp, deep_push_down_index},
    flat_concat,
    scheduled_execution::evaluate_schedule_adjust_numerical_scale,
    scheduled_execution::{
        circuit_to_schedule, circuit_to_schedule_naive_toposort, evaluate_schedule, SchedulingError,
    },
    CircuitNode, CircuitRc,
};
use crate::{
    py_types::{Tensor, UN_FLAT_CONCAT},
    timed,
    util::apply_fn_until_same,
};

// a lot of the function boundries in this are there because it would be too hard to optimize things jointly
// not because we don't need to optimize things jointly
// like scheduling does impact whether you should distribute, but using that info would be
// difficult

#[pyclass]
#[derive(Debug, Clone, Copy, PyClassDeriv)]
pub struct OptimizationSettings {
    #[pyo3(get, set)]
    pub verbose: usize,
    #[pyo3(get, set)]
    pub max_memory: usize,
    #[pyo3(get, set)]
    pub scheduling_num_mem_chunks: usize,
    #[pyo3(get, set)]
    pub distribute_min_size: usize,
    #[pyo3(get, set)]
    pub scheduling_naive: bool,
    #[pyo3(get, set)]
    pub scheduling_simplify: bool,
    #[pyo3(get, set)]
    pub adjust_numerical_scale: bool,
    #[pyo3(get, set)]
    pub numerical_scale_min: f64,
    #[pyo3(get, set)]
    pub numerical_scale_max: f64,
    #[pyo3(get, set)]
    pub capture_and_print: bool,
}

impl Default for OptimizationSettings {
    fn default() -> Self {
        Self {
            verbose: 0,
            max_memory: 9_000_000_000,
            scheduling_num_mem_chunks: 200,
            distribute_min_size: 800_000_000,
            scheduling_naive: false,
            scheduling_simplify: true,
            adjust_numerical_scale: false,
            numerical_scale_min: 1e-8,
            numerical_scale_max: 1e8,
            capture_and_print: false,
        }
    }
}

#[pymethods]
impl OptimizationSettings {
    #[new]
    #[args(
        verbose = "OptimizationSettings::default().verbose",
        max_memory = "OptimizationSettings::default().max_memory",
        scheduling_num_mem_chunks = "OptimizationSettings::default().scheduling_num_mem_chunks",
        distribute_min_size = "OptimizationSettings::default().distribute_min_size",
        scheduling_naive = "OptimizationSettings::default().scheduling_naive",
        scheduling_simplify = "OptimizationSettings::default().scheduling_simplify",
        adjust_numerical_scale = "OptimizationSettings::default().adjust_numerical_scale",
        numerical_scale_min = "OptimizationSettings::default().numerical_scale_min",
        numerical_scale_max = "OptimizationSettings::default().numerical_scale_max",
        capture_and_print = "OptimizationSettings::default().capture_and_print"
    )]
    fn new(
        verbose: usize,
        max_memory: usize,
        scheduling_num_mem_chunks: usize,
        distribute_min_size: usize,
        scheduling_naive: bool,
        scheduling_simplify: bool,
        adjust_numerical_scale: bool,
        numerical_scale_min: f64,
        numerical_scale_max: f64,
        capture_and_print: bool,
    ) -> Self {
        Self {
            verbose,
            max_memory,
            scheduling_num_mem_chunks,
            distribute_min_size,
            scheduling_naive,
            scheduling_simplify,
            adjust_numerical_scale,
            numerical_scale_min,
            numerical_scale_max,
            capture_and_print,
        }
    }
}

#[pyfunction]
pub fn optimize_circuit(circuit: CircuitRc, settings: OptimizationSettings) -> CircuitRc {
    let print_timings = settings.verbose >= 2;
    let circuit = timed!(strip_names(circuit), 10, print_timings);
    let circuit = timed!(deep_canonicalize(circuit), 10, print_timings);
    if settings.verbose >= 4 {
        println!("Original Circuit");
        circuit.compiler_print();
    }
    let circuit = timed!(compiler_simp(&circuit), 10, print_timings);
    // originally tried push_down_index in compiler_simp, but that produced worse circuits
    // for unknown reasons, maybe i'll investigate
    let circuit = timed!(deep_push_down_index(circuit, None), 10, print_timings);
    let circuit = timed!(compiler_simp(&circuit), 10, print_timings);
    let circuit = timed!(deep_canonicalize(circuit), 10, print_timings);
    if settings.verbose >= 3 {
        println!("Simplified Circuit");
        circuit.compiler_print();
    }
    let circuit = timed!(
        apply_fn_until_same(&circuit, &mut |x| compiler_simp(&deep_maybe_distribute(
            x, settings
        ))),
        10,
        print_timings
    );

    let circuit = timed!(deep_canonicalize(circuit), 10, print_timings);
    let circuit = timed!(deep_heuristic_nest_adds(circuit), 10, print_timings);

    let circuit = timed!(deep_optimize_einsums(circuit), 10, print_timings);

    let circuit = timed!(deep_canonicalize(circuit), 10, print_timings);
    if settings.verbose >= 3 {
        println!("Final Circuit");
        circuit.compiler_print();
    }
    circuit
}

#[pyfunction]
pub fn optimize_and_evaluate(
    circuit: CircuitRc,
    settings: OptimizationSettings,
) -> Result<Tensor, SchedulingError> {
    let verbose = settings.verbose;
    if verbose > 0 {
        println!("Optimizing verbose {}", verbose)
    }
    if settings.capture_and_print {
        println!("{}", rust_expression_notation_circuit(circuit.clone()));
    }
    let optimized_circuit = timed!(optimize_circuit(circuit, settings), 10, verbose >= 1);
    // return evaluate_fn(&*optimized_circuit).unwrap();
    let schedule = if settings.scheduling_naive {
        circuit_to_schedule_naive_toposort(optimized_circuit.clone())
    } else {
        timed!(
            circuit_to_schedule(optimized_circuit.clone(), settings),
            10,
            verbose >= 1
        )?
    };
    if verbose > 1 {
        println!("{}", schedule.get_stats());
    }
    let eval = || {
        if settings.adjust_numerical_scale {
            evaluate_schedule_adjust_numerical_scale(schedule, settings)
                [&optimized_circuit.info().hash]
                .clone()
        } else {
            evaluate_schedule(schedule)[&optimized_circuit.info().hash].clone()
        }
    };
    let out = timed!(eval(), 10, verbose >= 1);

    Ok(out)
}

/// in python, lots of functions take in collections of circuits and operate on them at once
/// with node caching for just that batch
/// because functions that take one circuit already cache nodes, it's convenient to compute multiple nodes
/// by flat-concatting and then passing around as one circuit
/// flat concatting then splitting is an extra copy on all return data,
/// which we could get rid of by removing flat-concat after rewrites (which would only work with a black box flat_concat node bc simplification isn't guaranteed to preserve concat at at end)
#[pyfunction]
pub fn optimize_and_evaluate_many(
    circuits: Vec<CircuitRc>,
    settings: OptimizationSettings,
) -> Result<Vec<Tensor>, SchedulingError> {
    let flat_concatted = flat_concat(circuits.clone()).rc();
    let evaluated = optimize_and_evaluate(flat_concatted, settings)?;
    let out = Python::with_gil(|py| {
        UN_FLAT_CONCAT
            .call(
                py,
                (
                    evaluated,
                    circuits
                        .iter()
                        .map(|x| x.info().shape.clone())
                        .collect::<Vec<Vec<usize>>>(),
                ),
                None,
            )
            .unwrap()
            .extract(py)
            .unwrap()
    });

    Ok(out)
}
