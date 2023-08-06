use std::collections::HashMap;

use super::{
    circuit_utils::{count_nodes, total_flops},
    repr::ReprWrapper,
    Circuit, CircuitNode, CircuitNodeUnion, CircuitRc, HashBytes,
};
use crate::circuit::repr::RustRepr;
use crate::toposort_circuit;
use num_bigint::BigUint;
use pyo3::pyfunction;

pub fn repr_circuit_deep_compiler(circuit: &Circuit) -> String {
    let mut seen_hashes: HashMap<HashBytes, String> = HashMap::new();
    fn recurse(
        circ: &Circuit,
        depth: usize,
        result: &mut String,
        seen_hashes: &mut HashMap<HashBytes, String>,
    ) {
        result.push_str(&" ".repeat(depth * 2));
        if let Some(prev) = seen_hashes.get(&circ.info().hash) {
            result.push_str(prev);
            result.push('\n');
            return;
        }
        seen_hashes.insert(
            circ.info().hash,
            seen_hashes.len().to_string() + " " + circ.name().unwrap_or(&circ.variant_string()),
        );
        result.push_str(&(seen_hashes.len() - 1).to_string());
        if let Some(n) = circ.name() {
            result.push_str(n);
            result.push(' ');
        }
        result.push_str(&format!("{:?}", circ.info().shape));
        result.push(' ');
        if circ.info().numel() > BigUint::from(400_000_000usize)
            && !matches!(circ, Circuit::ArrayConstant(_))
        {
            result.push_str(&format!(
                "\u{001b}[31m{}\u{001b}[0m ",
                oom_fmt(circ.info().numel())
            ));
        }
        result.push_str(&circ.variant_string());
        result.push(' ');
        result.push_str(&{
            match circ {
                Circuit::ScalarConstant(scalar) => format!("{:10.5e}", scalar.value),
                Circuit::Rearrange(rearrange) => rearrange.spec.to_einops_string(),
                Circuit::Einsum(einsum) => einsum.get_spec().to_einsum_string(),
                Circuit::Index(index) => format!("{}", index.index),
                Circuit::Scatter(scatter) => format!("{}", scatter.index),
                Circuit::Concat(concat) => concat.axis.to_string(),
                Circuit::GeneralFunction(gf) => gf.spec.name.clone(),
                Circuit::Symbol(sy) => format!("{}", &sy.uuid),
                _ => "".to_owned(),
            }
        });
        if circ.info().named_axes.iter().any(|x| x.is_some()) {
            result.push_str(&format!(
                " NA[{}]",
                circ.info()
                    .named_axes
                    .iter()
                    .map(|x| match x {
                        None => "".to_owned(),
                        Some(s) => s.clone(),
                    })
                    .collect::<Vec<_>>()
                    .join(",")
            ))
        }
        result.push('\n');
        for child in circ.children() {
            recurse(&child, depth + 1, result, seen_hashes);
        }
    }
    let mut result = String::new();
    recurse(circuit, 0, &mut result, &mut seen_hashes);
    result
}

pub fn oom_fmt<T: Into<BigUint>>(num: T) -> String {
    let mut num: BigUint = num.into();
    let k = BigUint::from(1000usize);
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"].iter() {
        if &num < &k {
            return format!("{}{}", num, unit);
        }
        num /= &k;
    }
    format!("{}Y", num)
}

/// gets a Rust expression that will evaluate to the circuit, assuming children are already constructed.
/// context maps children to variable names.
/// we use a top sort to determine to order of calls to this function so that
/// context always has the names for circuits we'll need to repr this one
pub fn repr_circuit_one_level(circuit: &CircuitRc, context: &HashMap<CircuitRc, String>) -> String {
    let node_string = |x: &CircuitRc| format!("{}.clone()", context[x]);
    match circuit.as_ref() {
        Circuit::Einsum(e) => {
            let einargs = e
                .args
                .iter()
                .map(|(c, ax)| ReprWrapper(format!("({}, {})", node_string(c), ax.repr())))
                .collect::<Vec<ReprWrapper>>()
                .repr();
            format!(
                "Einsum::nrc({}, {}, {})",
                einargs,
                e.out_axes.repr(),
                e.name_cloned().repr()
            )
        }
        Circuit::ArrayConstant(a) => format!(
            "ArrayConstant::randn_named_seeded({}, {}, {}).rc()",
            a.compute_shape().repr(),
            a.name_cloned().repr(),
            a.value.hash_usize().unwrap(),
        ),
        Circuit::Symbol(s) => format!(
            "Symbol::nrc({}, {}, {})",
            s.compute_shape().repr(),
            s.uuid.repr(),
            s.name_cloned().repr()
        ),
        Circuit::ScalarConstant(s) => format!(
            "ScalarConstant::nrc({}, {}, {})",
            s.value.repr(),
            s.compute_shape().repr(),
            s.name_cloned().repr()
        ),
        Circuit::Add(a) => {
            let variable_names: Vec<String> = a.children().map(|c| node_string(&c)).collect();
            format!(
                "Add::nrc(vec![{}], {})",
                variable_names.join(", "),
                a.name_cloned().repr()
            )
        }
        Circuit::Rearrange(r) => {
            format!(
                "Rearrange::nrc({}, {}, {})",
                node_string(&r.node),
                r.spec.repr(),
                r.name_cloned().repr()
            )
        }
        Circuit::Index(i) => format!(
            "Index::nrc({}, {}, {})",
            node_string(&i.node),
            i.index.repr(i.node.info().shape.clone()),
            i.name_cloned().repr()
        ),
        Circuit::GeneralFunction(g) => {
            if g.spec.is_official {
                let variable_names: Vec<String> = g.children().map(|x| node_string(&x)).collect();
                format!(
                    "GeneralFunction::new_by_name(vec![{}], {}, {}).unwrap().rc()",
                    variable_names.join(", "),
                    g.spec.name.repr(),
                    g.name_cloned().repr()
                )
            } else {
                panic!("cant print non-official generalfunctions");
            }
        }
        Circuit::Concat(c) => {
            let variable_names: Vec<String> = c.children().map(|x| node_string(&x)).collect();
            format!(
                "Concat::nrc(vec![{}], {}, {})",
                variable_names.join(", "),
                c.axis,
                c.name_cloned().repr()
            )
        }
        Circuit::Scatter(s) => {
            format!(
                "Scatter::nrc({}, {}, {}, {})",
                node_string(&s.node),
                // indices are into the output zero-padded array, so we use the shape of s instead of s.node
                s.index.repr(s.info().shape.clone()),
                s.compute_shape().repr(),
                s.name_cloned().repr()
            )
        }
    }
}

/// Prints out a string of Rust code representing an expression that evaluates to the
/// circuit provided
/// There's an analogous Python function, interp.circuit.print_circuit.lambda_notation_circuit
///
/// Python example:
/// >>> import rust_circuit
/// >>> a = rust_circuit.ScalarConstant(0.2, (3,), 'a')
/// >>> b = rust_circuit.ScalarConstant(0.5, (3,))
/// >>> s = rust_circuit.Add([a, b], 's')
/// >>> q = rust_circuit.Concat([a, s], 0, 'cat')
/// >>> print(rust_circuit.rust_expression_notation_circuit(q))
///
/// This will give the following code (`use` and final `;` added for doctest):
/// ```
/// use rust_circuit::circuit::*;
/// {
///     let node0 = ScalarConstant::new(0.2, vec![3], Some("a".to_owned())).rc();
///     let node1 = ScalarConstant::new(0.5, vec![3], Some("ScalarConstant".to_owned())).rc();
///     let node2 = Add::nrc(vec![node0.clone(), node1.clone()], Some("s".to_owned())).rc();
///     Concat::nrc(vec![node0.clone(), node2.clone()], 0, Some("cat".to_owned())).rc()
/// };
/// ```
#[pyfunction]
pub fn rust_expression_notation_circuit(circuit: CircuitRc) -> String {
    // Possible improvements:
    // * better variable names (if the node has a name that is a valid Rust identifier, doesn't shadow anything, ..., use that)
    // * inline single use variables?

    // context/environment of circuit variable names so far
    let mut context: HashMap<CircuitRc, String> = HashMap::new();

    // make a source code block defining each node in a topologically sorted order
    let order = toposort_circuit(circuit);
    let mut source = String::with_capacity(order.len() * 60);
    source.push_str("{\n");

    for (i, node) in order.iter().enumerate() {
        // we will use the very creative naming scheme of node0, node1, ...
        // later we should leverage the names most nodes already have
        // (needs to be unique, a valid Rust identifier, and can't shadow important stuff)
        let key: CircuitRc = CircuitRc(node.0.clone());
        context.insert(key.clone(), format!("node{}", i));

        let node_source = repr_circuit_one_level(node, &context);
        if i < order.len() - 1 {
            source.push_str(format!("    let {} = {};\n", context[node], node_source).as_str());
        } else {
            // the block needs to return the top level circuit, which is the last element of the top sort
            source.push_str(format!("    {}\n", node_source).as_str());
        }
    }
    source.push_str("}");
    source
}

#[rustfmt::skip]
#[test]
fn slightly_test_expression_notation_circuit() {
    use crate::{
        circuit::{
            circuit_utils::replace_all_randn_seeded, Add, ArrayConstant, Concat, Einsum,
            GeneralFunction, Index, Rearrange, ScalarConstant, Scatter, Symbol,
        },
        rearrange_spec::OpSize,
        rearrange_spec::RearrangeSpec,
        tensor_util::Slice,
        tensor_util::{TensorAxisIndex, TensorIndex},
    };
    use uuid::uuid;
    pyo3::prepare_freethreaded_python();
    let array = ArrayConstant::randn_named_seeded(vec![2, 4, 3, 4], None, 1861206500329984137).rc();
    let circuit2 = Einsum::nrc(
        vec![(
            Add::nrc(
                vec![
                    Rearrange::nrc(
                        Index::nrc(
                            array.clone(),
                            TensorIndex(vec![
                                TensorAxisIndex::Single(0),
                                TensorAxisIndex::new_plain_slice(0, 2),
                                TensorAxisIndex::IDENT,
                                TensorAxisIndex::new_tensor_randint_seeded(4, 4, 0),
                            ]),
                            None,
                        ),
                        RearrangeSpec::ident(3),
                        None,
                    ),
                    Concat::nrc(vec![ScalarConstant::nrc(2.2, vec![2, 3, 4], None)], 0, None),
                    Scatter::nrc(
                        Symbol::nrc(
                            vec![2, 3, 4],
                            uuid!("20fd28de-09d9-4773-8f0f-97dcceb855c8"),
                            None,
                        ),
                        TensorIndex::ident(3),
                        vec![2, 3, 4],
                        None,
                    ),
                ],
                None,
            ),
            vec![0, 1, 2],
        )],
        vec![0, 1],
        None,
    );
    println!(
        "{:?}",
        array.as_array_constant().unwrap().value.hash_usize()
    );
    println!("{}", rust_expression_notation_circuit(circuit2.clone()));
    let circuit2back = {
    let node0 = ScalarConstant::nrc(2.2_f64, vec![2,3,4], None);
    let node1 = Symbol::nrc(vec![2,3,4], uuid!("20fd28de-09d9-4773-8f0f-97dcceb855c8"), None);
    let node2 = Scatter::nrc(node1.clone(), TensorIndex ( vec![TensorAxisIndex::Slice(Slice { start:None, stop:None }), TensorAxisIndex::Slice(Slice { start:None, stop:None }), TensorAxisIndex::Slice(Slice { start:None, stop:None })] ), vec![2,3,4], None);
    let node3 = ArrayConstant::randn_named_seeded(vec![2,4,3,4], None, 10357450781205879365).rc();
    let node4 = Index::nrc(node3.clone(), TensorIndex ( vec![TensorAxisIndex::Single(0), TensorAxisIndex::Slice(Slice { start:Some(0), stop:Some(2) }), TensorAxisIndex::Slice(Slice { start:None, stop:None }), TensorAxisIndex::new_tensor_randint_seeded(4,4,8895353701350677791)] ), None);
    let node5 = Concat::nrc(vec![node0.clone()], 0, None);
    let node6 = Rearrange::nrc(node4.clone(), RearrangeSpec::new(vec![vec![0],vec![1],vec![2]], vec![vec![0],vec![1],vec![2]], vec![OpSize::from(None),OpSize::from(None),OpSize::from(None)]), None);
    let node7 = Add::nrc(vec![node6.clone(), node5.clone(), node2.clone()], None);
    Einsum::nrc(vec![(node7.clone(), vec![0,1,2])], vec![0,1], None)
};
    assert_eq!(replace_all_randn_seeded(circuit2), circuit2back);
}

pub fn print_circuit_stats(circuit: &Circuit) {
    let mut result = String::new();
    result.push_str(
        &circuit
            .name_cloned()
            .map(|x| x + " ")
            .unwrap_or(" ".to_owned()),
    );
    result.push_str(&circuit.variant_string());
    result.push_str(&format!(
        " nodes {} max_size {} flops {}",
        count_nodes(circuit.clone().rc()),
        oom_fmt(circuit.max_non_input_size()),
        oom_fmt(total_flops(circuit.clone().rc()))
    ));
    println!("{}", result);
}
