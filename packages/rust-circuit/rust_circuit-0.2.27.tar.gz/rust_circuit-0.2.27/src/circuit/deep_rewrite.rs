use std::collections::{HashMap, HashSet};

use crate::pyo3_prelude::*;
use itertools::Itertools;
use num_bigint::BigUint;

use crate::{
    cached_circuit_lambda,
    circuit::diag_rewrite::{add_pull_diags, einsum_push_down_trace},
    util::{apply_fn_until_same, mapping_until_end, AsOp},
};

use super::{
    algebraic_rewrite::*,
    canonicalize::{canonicalize_node, deep_canonicalize},
    concat_rewrite::add_pull_concat,
    concat_rewrite::{
        concat_drop_size_zero, concat_fuse, einsum_pull_concat, generalfunction_pull_concat,
        index_concat_drop_unreached,
    },
    deep_map_unwrap, deep_map_unwrap_preorder,
    scatter_rewrite::{
        add_pull_scatter, einsum_pull_scatter, index_einsum_to_scatter, scatter_elim_identity,
        scatter_fuse, scatter_pull_removable_axes,
    },
    visit_circuit, Add, Circuit, CircuitNode, CircuitRc, Concat, GeneralFunction, HashBytes, Index,
};

/// seperate _py function because pyfunctions cant take reference arguments
#[pyfunction]
#[pyo3(name = "compiler_simp_step")]
pub fn compiler_simp_step_py(circ: CircuitRc) -> Option<CircuitRc> {
    compiler_simp_step(&circ)
}

pub fn compiler_simp_step(circuit: &Circuit) -> Option<CircuitRc> {
    macro_rules! f_wrap {
        ($f:expr) => {
            &|x| $f(x).map(|v| v.rc())
        };
    }

    fn simp<'a, T: CircuitNode + Into<Circuit> + Clone>(
        x: &'a T,
        fns: &[&dyn Fn(&'a T) -> Option<CircuitRc>],
    ) -> Option<CircuitRc> {
        for f in fns {
            if let Some(result) = f(x) {
                if **result == x.clone().c() {
                    println!("{}", stringify!(f));
                    x.clone().rc().compiler_print();
                    result.compiler_print();
                    panic!()
                }
                return Some(result);
            }
        }

        None
    }

    match &*circuit {
        Circuit::Add(node) => {
            let fns: &[&dyn Fn(_) -> _] = &[
                &remove_add_few_input,
                f_wrap!(add_flatten_once),
                f_wrap!(add_elim_zeros),
                f_wrap!(add_collapse_scalar_inputs),
                &f_wrap!(add_deduplicate),
                &|x| add_pull_removable_axes(x, true),
                &f_wrap!(add_pull_scatter),
                &f_wrap!(add_pull_diags),
            ];
            simp(node, fns)
        }
        Circuit::Einsum(node) => {
            let fns: &[&dyn Fn(_) -> _] = &[
                f_wrap!(&einsum_elim_zero),
                &einsum_elim_identity,
                f_wrap!(&einsum_flatten_once),
                f_wrap!(&einsum_of_permute_merge),
                f_wrap!(&einsum_merge_scalars),
                &einsum_pull_removable_axes,
                &einsum_pull_scatter,
                f_wrap!(&einsum_push_down_trace),
                // &einsum_pull_concat,
            ];
            simp(node, fns)
        }
        Circuit::Index(node) => {
            let fns: &[&dyn Fn(_) -> _] = &[
                &index_elim_identity,
                f_wrap!(&index_fuse),
                &index_merge_scalar,
                &index_einsum_to_scatter,
                &index_concat_drop_unreached,
            ];
            simp(node, fns)
        }
        Circuit::Rearrange(node) => {
            let fns: &[&dyn Fn(_) -> _] = &[
                &rearrange_elim_identity,
                f_wrap!(&rearrange_fuse),
                &rearrange_merge_scalar,
                f_wrap!(&permute_of_einsum_merge),
            ];
            simp(node, fns)
        }
        Circuit::Concat(node) => {
            let fns: &[&dyn Fn(&Concat) -> _] = &[
                &concat_elim_identity,
                &concat_pull_removable_axes,
                &concat_merge_uniform,
                f_wrap!(&concat_drop_size_zero),
                f_wrap!(&concat_fuse),
                f_wrap!(&concat_repeat_to_rearrange),
            ];
            simp(node, fns)
        }
        Circuit::GeneralFunction(node) => {
            let fns: &[&dyn Fn(&GeneralFunction) -> _] = &[
                &generalfunction_pull_removable_axes,
                &generalfunction_evaluate_simple,
                // f_wrap!(&generalfunction_pull_concat),
            ];
            simp(node, fns)
        }
        Circuit::Scatter(node) => {
            let fns: &[&dyn Fn(_) -> _] = &[
                &scatter_elim_identity,
                f_wrap!(&scatter_fuse),
                f_wrap!(&scatter_pull_removable_axes),
            ];
            simp(node, fns)
        }
        _ => None,
    }
}

// deep simplification strategy

// if you just do preorder or postorder mapping, you might need to run simp O(circuit_depth) times
// because pull_removable_axes or such could bubble up
// this would make simp to convergence O(circuit_nodes*circuit_depth)

// what's currently implemented is: simplify from bottom up, whenever a node is changed by simplification,
// simplify its children and grandchildren, going down farther if those change
// currently all simplification rewrites only change the grandchildren, not great-grandchildren
// so this converges on one pass, and takes O(circuit_nodes+simplification_steps_needed) time

// a better algorithm would be bottom up, whenever one changes check down until you see nodes that
// you've simplified before. that would remove the dont-change-great-grandchildren requirement

pub fn compiler_simp_down_if_here(circ: &Circuit) -> Option<CircuitRc> {
    compiler_simp_step(circ).and_then(|x| compiler_simp_down(&x))
}

pub fn compiler_simp_down_one(circ: &Circuit) -> Option<CircuitRc> {
    let simp_here = compiler_simp_step(circ);
    if let Some(x) = simp_here {
        return Some(compiler_simp_down(&x).unwrap_or(x));
    }
    circ.map_children_op(&mut compiler_simp_down_if_here)
        .map(|x| x.rc())
}

pub fn compiler_simp_down(circ: &Circuit) -> Option<CircuitRc> {
    // if remaining_stack().unwrap()<3_000_000{
    //     println!("jank recursion limit reached");
    //     circ.compiler_print();
    //     panic!();
    // }
    let simp_here = compiler_simp_step(circ);
    if let Some(x) = simp_here {
        return Some(compiler_simp_down(&x).unwrap_or(x));
    }
    circ.map_children_op(&mut compiler_simp_down_one)
        .map(|x| x.rc())
}

#[pyfunction]
#[pyo3(name = "compiler_simp")]
pub fn compiler_simp_py(circ: CircuitRc) -> CircuitRc {
    compiler_simp(&circ)
}

/// this simplifies individual nodes from the bottom up.
/// whenever a node is simplified, its grandchildren are simplified, but great grandchildren aren't
/// this is meant to catch all simplifications given that individual rewrites don't change great grandchildren
pub fn compiler_simp(circ: &Circuit) -> CircuitRc {
    cached_circuit_lambda! {
        let mut recurse = |circ: CircuitRc| -> CircuitRc = {
            let mut result: CircuitRc = circ.map_children_unwrap(&mut |x:&Circuit|recurse(x.clone().rc())).rc();
            for iter_count in 0.. {
                match compiler_simp_step(&result) {
                    Some(r) => result = compiler_simp_down(&r).unwrap_or(r),
                    None => {
                        break;
                    }
                }
                // result.compiler_print();
                if iter_count > 50 {
                    println!("here");
                    result.compiler_print();
                    compiler_simp_step(&result).unwrap().compiler_print();
                    panic!();
                }
            }
            result
        };
    };
    recurse(circ.clone().rc())
}

#[pyfunction]
pub fn compiler_simp_until_same(circ: CircuitRc) -> CircuitRc {
    apply_fn_until_same(&circ, &mut |x: &CircuitRc| compiler_simp(x))
}

#[pyfunction]
pub fn deep_push_down_index(circ: CircuitRc, min_size: Option<usize>) -> CircuitRc {
    deep_map_unwrap_preorder(&circ, &|circ| {
        if min_size.is_none()
            || circ
                .children()
                .chain(std::iter::once(circ.clone().rc()))
                .any(|z| z.info().numel() >= BigUint::from(min_size.unwrap()))
        {
            circ.and_then_or_clone(&|index: &Index| {
                push_down_index(&index.and_then_or_clone(index_fuse))
            })
        } else {
            circ.clone().rc()
        }
    })
}

/// we want adds to be nested rather than flat so arguments can be dropped if they're only needed
/// in future adds
/// this is suboptimal in many ways. one is broadcasts allow outer products which should be avoided but aren't
/// for each add, greedily nest into preexisting adds
#[pyfunction]
pub fn deep_heuristic_nest_adds(circ: CircuitRc) -> CircuitRc {
    let circ = deep_canonicalize(circ);
    let mut seen_adds: HashSet<Add> = HashSet::new();
    let mut mapping: HashMap<Add, Add> = HashMap::new();
    visit_circuit(&circ, &mut |c: &Circuit| {
        if let Some(add) = c.as_add() {
            seen_adds.insert(add.clone());
        }
    });
    let mut intersections: HashSet<Add> = HashSet::new();
    for circ in &seen_adds {
        for circ2 in &seen_adds {
            let intersection = Add::try_new(
                circ.nodes
                    .iter()
                    .filter(|x| circ2.nodes.contains(x))
                    .cloned()
                    .collect(),
                None,
            )
            .unwrap();
            if intersections.len() >= 2 && &intersection != circ && &intersection != circ2 {
                intersections.insert(intersection);
            }
        }
    }
    seen_adds.extend(intersections);
    while let Some((sub, sup)) = (|| {
        for cand_sub in &seen_adds {
            if cand_sub.nodes.iter().unique().count() > 1 {
                for cand_sup in &seen_adds {
                    if cand_sub != cand_sup
                        && cand_sub.nodes.iter().all(|x| cand_sup.nodes.contains(x))
                    {
                        return Some((cand_sub.clone(), cand_sup.clone()));
                    }
                }
            }
        }
        None
    })() {
        seen_adds.remove(&sup);
        let new_sup = canonicalize_node(
            &Add::try_new(
                sup.nodes
                    .iter()
                    .cloned()
                    .filter(|x| !sub.nodes.contains(x))
                    .chain(std::iter::once(sub.clone().rc()))
                    .collect(),
                None,
            )
            .unwrap()
            .rc(),
        );
        let new_sup = new_sup.as_add().unwrap();
        seen_adds.insert(new_sup.clone());
        mapping.insert(sup, new_sup.clone());
    }
    deep_map_unwrap_preorder(&circ, &|c| {
        c.map_or_clone(|add| {
            let add = mapping_until_end(add, &mapping);

            if add.info().numel() > BigUint::from(100_000_000usize) {
                add_nest_ltr(&add)
            } else {
                add
            }
        })
    })
}

pub fn add_nest_ltr(add: &Add) -> Add {
    let mut result = add.clone();
    while result.nodes.len() > 2 {
        result = Add::try_new(
            std::iter::once(
                Add::try_new(vec![result.nodes[0].clone(), result.nodes[1].clone()], None)
                    .unwrap()
                    .rc(),
            )
            .chain(result.nodes.iter().dropping(2).cloned())
            .collect::<Vec<CircuitRc>>(),
            None,
        )
        .unwrap();
    }
    result
}

#[pyfunction]
pub fn deep_pull_concat_messy(circuit: CircuitRc, min_size: Option<usize>) -> CircuitRc {
    deep_map_unwrap(&circuit, &|x: &Circuit| {
        if min_size.is_none()
            || x.children()
                .chain(std::iter::once(x.clone().rc()))
                .any(|z| z.info().numel() >= BigUint::from(min_size.unwrap()))
        {
            match x {
                Circuit::Add(add) => add.and_then_or_clone(add_pull_concat),
                Circuit::GeneralFunction(func) => {
                    func.and_then_or_clone(generalfunction_pull_concat)
                }
                Circuit::Einsum(einsum) => einsum.and_then_or_clone(einsum_pull_concat),
                Circuit::Concat(concat) => concat.and_then_or_clone(concat_fuse),
                _ => x.clone().rc(),
            }
        } else {
            x.clone().rc()
        }
    })
}

#[pyfunction]
pub fn deep_pull_concat(circuit: CircuitRc, min_size: Option<usize>) -> CircuitRc {
    let pulled = deep_pull_concat_messy(circuit, min_size);
    apply_fn_until_same(&pulled, &mut |x: &CircuitRc| {
        deep_push_down_index(compiler_simp(x), min_size)
    })
}
