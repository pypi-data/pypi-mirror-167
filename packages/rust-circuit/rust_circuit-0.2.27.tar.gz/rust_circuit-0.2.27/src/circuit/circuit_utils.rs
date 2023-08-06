use std::collections::{BTreeSet, HashMap};

use crate::{opt_einsum::EinsumSpec, pyo3_prelude::*};
use num_bigint::BigUint;

use super::{
    deep_map_unwrap, visit_circuit, ArrayConstant, Circuit, CircuitNode, CircuitRc, HashBytes,
};
use crate::{tensor_util::TorchDeviceDtype, util::AsOp};

#[pyfunction]
pub fn cast_circuit(circ: CircuitRc, device_dtype: &TorchDeviceDtype) -> CircuitRc {
    deep_map_unwrap(&circ, &|circ| {
        circ.map_or_clone(|node: &ArrayConstant| {
            ArrayConstant::new(
                device_dtype.cast_tensor(node.value.clone()),
                node.name_cloned(),
            )
        })
    })
}

#[pyfunction]
pub fn count_nodes(circuit: CircuitRc) -> usize {
    let mut result: usize = 0;
    visit_circuit(&circuit, &mut |_x: &Circuit| result += 1);
    result
}

pub fn hash_to_node(circuit: &Circuit) -> HashMap<HashBytes, CircuitRc> {
    let mut result: HashMap<HashBytes, CircuitRc> = HashMap::new();
    visit_circuit(circuit, &mut |x: &Circuit| {
        result.insert(x.info().hash, x.clone().rc());
    });
    result
}

#[pyfunction]
pub fn total_flops(circuit: CircuitRc) -> BigUint {
    let mut result: BigUint = BigUint::from(0usize);
    visit_circuit(&circuit, &mut |x: &Circuit| result += x.self_flops());
    result
}

#[pyfunction]
pub fn total_arrayconstant_size(circuit: CircuitRc) -> BigUint {
    let mut result: BigUint = BigUint::from(0usize);
    visit_circuit(&circuit, &mut |x: &Circuit| {
        if let Circuit::ArrayConstant(x) = x {
            result += x.info().numel();
        }
    });
    result
}
#[pyfunction]
pub fn sum_of_node_sizes(circuit: CircuitRc) -> BigUint {
    let mut result: BigUint = BigUint::from(0usize);
    visit_circuit(&circuit, &mut |x: &Circuit| {
        if !matches!(x, Circuit::ArrayConstant(_)) {
            result += x.info().numel();
        }
    });
    result
}

#[pyfunction]
pub fn get_leaves(circuit: CircuitRc) -> Vec<CircuitRc> {
    let mut result: Vec<CircuitRc> = vec![];
    visit_circuit(&circuit, &mut |c: &Circuit| {
        if c.children().count() == 0 {
            result.push(c.clone().rc());
        }
    });
    result
}

#[pyfunction]
pub fn get_all_einsum_specs(circuit: CircuitRc) -> Vec<EinsumSpec> {
    let mut result: Vec<EinsumSpec> = vec![];
    visit_circuit(&**circuit, &mut |c| {
        if let Circuit::Einsum(node) = c {
            result.push(node.get_spec());
        }
    });
    result
}

#[pyfunction]
pub fn toposort_circuit(circuit: CircuitRc) -> Vec<CircuitRc> {
    let mut num_refs: HashMap<CircuitRc, usize> = HashMap::new();
    visit_circuit(&circuit, &mut |c| {
        for child in c.children() {
            *num_refs.entry(child).or_insert(0) += 1;
        }
    });
    let mut ready: BTreeSet<CircuitRc> = BTreeSet::from([circuit.clone()]);
    let mut result: Vec<CircuitRc> = vec![];
    while !ready.is_empty() {
        let here = ready.pop_first().unwrap();
        for child in here.children() {
            num_refs.insert(child.clone(), num_refs[&child] - 1);
            if num_refs[&child] == 0 {
                ready.insert(child);
            }
        }
        result.push(here.clone())
    }
    result.reverse();
    result
}

pub fn deep_map_pass_up<F, T>(circuit: &Circuit, f: &mut F) -> (CircuitRc, T)
where
    T: Clone,
    F: FnMut(&Circuit, Vec<T>) -> (CircuitRc, T),
{
    let topo = toposort_circuit(circuit.clone().rc());
    let mut pass_ups: HashMap<CircuitRc, T> = HashMap::new();
    for c in topo {
        let passed_up = c.children().map(|c| pass_ups[&c].clone()).collect();
        let (new, pass_here) = f(&c, passed_up);
        pass_ups.insert(c.clone(), pass_here.clone());
        if &**c == circuit {
            return (new, pass_here);
        }
    }
    panic!();
}

// pub fn deep_map_pass_down<F, T>(circuit: &Circuit, f: &mut F) -> CircuitRc
// where
//     T: Clone,
//     F: FnMut(&Circuit, Vec<T>) -> (CircuitRc, Vec<T>),
// {
//     let mut topo = toposort_circuit(circuit);
//     topo.reverse();
//     let mut pass_downs: HashMap<CircuitRc, Vec<T>> = HashMap::new();
//     for c in topo {
//         let passed_down = pass_downs.remove(&c).unwrap();
//         let (new, pass_here) = f(&c, passed_down);
//         for (child,passed) in zip(c.children(),pass_here){
//             pass_downs.entry(child).or_insert(vec![]).push(passed);
//         }
//         if &**c == circuit {
//             return (new, pass_here);
//         }
//     }
//     panic!();
// }
