mod solver;

use pyo3::prelude::*;

use lazy_static::lazy_static;
lazy_static! {
    static ref SOLVER: solver::Solver = solver::Solver::new();
}

#[pyfunction]
fn shanten(hand: Vec<usize>) -> PyResult<i32> {
    if hand.len() != 34 {
        panic!("hand.len() must be 34");
    }
    let size = hand.iter().sum();
    match size {
        13 | 14 => {
            Ok(SOLVER.shanten(&hand, 0))
        }
        10 | 11 => {
            Ok(SOLVER.shanten(&hand, 1))
        }
        7 | 8 => {
            Ok(SOLVER.shanten(&hand, 2))
        }
        4 | 5 => {
            Ok(SOLVER.shanten(&hand, 3))
        }
        1 | 2 => {
            Ok(SOLVER.shanten(&hand, 4))
        }
        _ => panic!("hand.iter().sum() must be 1, 2, 4, 5, 7, 8, 10, 11, 13 or 14")
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn shanten_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(shanten, m)?)?;
    Ok(())
}