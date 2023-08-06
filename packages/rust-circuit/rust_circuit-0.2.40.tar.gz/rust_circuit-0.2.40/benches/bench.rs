#![feature(test)]

use rust_circuit::circuit::circuit_optimizer::optimize_and_evaluate;

use rand::Rng;
use rust_circuit::opt_einsum::EinsumSpec;
// #[cfg(test)]

extern crate test;

pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {

    use super::*;
    use rust_circuit::{
        circuit::{Add, ArrayConstant, CircuitNode, Einsum, GeneralFunction},
        tensor_util::TorchDeviceDtypeOp,
    };
    use test::Bencher;

    #[test]
    fn it_works() {
        assert_eq!(4, add_two(2));
    }

    #[bench]
    pub fn bench_worst_case(bencher: &mut Bencher) {
        bencher.iter(|| {
            let n_operands = 15;
            let operand_width = 6;
            let n_ints = 10;
            let example = EinsumSpec {
                input_ints: (0..n_operands)
                    .map(|_i| {
                        (0..operand_width)
                            .map(|_j| rand::thread_rng().gen_range(0..n_ints))
                            .collect()
                    })
                    .collect(),
                output_ints: vec![0, 1, 2, 3, 4],
                int_sizes: (0..n_ints).collect(),
            };
            // println!("have einspec {:?}", example);
            // ('abc,abdc,d->abd', {0: 32768, 1: 8, 2: 32, 3: 35})
            let _opted = example.optimize_dp(None, None, Some(500));

            // println!("result {:?}", opted);
        })
    }

    #[bench]
    fn bench_opt_evaluate(bencher: &mut Bencher) {
        bencher.iter(|| {
            let circuit = Einsum::nrc(
                vec![(
                    Add::nrc(
                        vec![
                            ArrayConstant::randn_named(
                                vec![2, 3, 4],
                                None,
                                TorchDeviceDtypeOp::default(),
                            )
                            .rc(),
                            GeneralFunction::new_by_name(
                                vec![ArrayConstant::randn_named(
                                    vec![2, 3, 4],
                                    None,
                                    TorchDeviceDtypeOp::default(),
                                )
                                .rc()],
                                "sigmoid".to_owned(),
                                None,
                            )
                            .unwrap()
                            .rc(),
                        ],
                        None,
                    ),
                    vec![0, 1, 2],
                )],
                vec![0, 1],
                None,
            );
            optimize_and_evaluate(circuit, Default::default())
        });
    }
}
