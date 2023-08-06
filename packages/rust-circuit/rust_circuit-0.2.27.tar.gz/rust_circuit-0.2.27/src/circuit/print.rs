use std::collections::HashMap;

use num_bigint::BigUint;

use super::{
    circuit_utils::{count_nodes, total_flops},
    Circuit, CircuitNode, CircuitNodeUnion, HashBytes,
};

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
