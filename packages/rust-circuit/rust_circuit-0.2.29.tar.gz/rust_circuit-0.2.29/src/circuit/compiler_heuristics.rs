use crate::pyo3_prelude::*;
use num_bigint::BigUint;

use super::{
    algebraic_rewrite::{add_outer_product_broadcasts_on_top, distribute, get_removable_axes},
    circuit_optimizer::OptimizationSettings,
    circuit_utils::{sum_of_node_sizes, total_flops},
    deep_map_op,
    deep_rewrite::compiler_simp,
    Circuit, CircuitNode, CircuitRc, Einsum,
};

#[pyfunction]
/// only is reasonable if adds have gone through add_pull_removable, but meant to not crash otherwise
/// this is simpler than python version, maybe worse than it
pub fn maybe_distribute(node: &Einsum, settings: OptimizationSettings) -> Option<CircuitRc> {
    for (i, operand) in node.children().enumerate() {
        if node.max_non_input_size() >= BigUint::from(settings.distribute_min_size)
            && let Circuit::Add(add) = &**operand
            && (add_outer_product_broadcasts_on_top(add).is_some() ||  add.children().any(|child| {
                !get_removable_axes(&child).is_empty()
                || matches!(&**child, Circuit::Einsum(_) | Circuit::Scatter(_))
               }))

        {
            let noderc = node.clone().rc();
            let result = compiler_simp(&distribute(node, i, true).unwrap().rc());
            if result.info().max_non_input_size < node.info().max_non_input_size ||total_flops(result.clone())<total_flops(noderc.clone())||sum_of_node_sizes(result.clone())<sum_of_node_sizes(noderc){
                return Some(result);
            }
        }
    }
    None
}

#[pyfunction]
#[pyo3(name = "deep_maybe_distribute")]
pub fn deep_maybe_distribute_py(node: CircuitRc, settings: OptimizationSettings) -> CircuitRc {
    deep_maybe_distribute(&node, settings)
}

pub fn deep_maybe_distribute(node: &Circuit, settings: OptimizationSettings) -> CircuitRc {
    deep_map_op(node, &mut |x: &Circuit| match x {
        Circuit::Einsum(ein) => maybe_distribute(ein, settings),
        _ => None,
    })
    .unwrap_or(node.clone().rc())
}
