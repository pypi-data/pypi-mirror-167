use crate::pyo3_prelude::*;

use super::{
    circuit_node_private::CircuitNodePrivate, deep_map_unwrap, Circuit, CircuitNode, CircuitRc,
};

#[pyfunction]
pub fn strip_names(circuit: CircuitRc) -> CircuitRc {
    fn strip(circuit: &Circuit) -> CircuitRc {
        let mut result = circuit.clone();
        *result.name_mut() = None;
        result.rc()
    }
    deep_map_unwrap(&circuit, &strip)
}
