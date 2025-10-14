#[allow(dead_code)]
struct Solution;

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

fn neighbours(grid: &[Vec<i32>], row: usize, col: usize) -> Vec<(usize, usize)> {
    let (rows, cols) = (grid.len(), grid[0].len());

    let mut res = Vec::new();

    for (neigh_row_opt, neigh_col_opt) in [
        (Some(row + 1), Some(col)),
        (Some(row), Some(col + 1)),
        (row.checked_sub(1), Some(col)),
        (Some(row), col.checked_sub(1)),
        (row.checked_sub(1), Some(col + 1)),
        (Some(row + 1), Some(col + 1)),
        (row.checked_add(1), col.checked_sub(1)),
        (row.checked_sub(1), col.checked_sub(1)),
    ] {
        if let (Some(neigh_row), Some(neigh_col)) = (neigh_row_opt, neigh_col_opt) {
            if neigh_row < rows && neigh_col < cols && grid[neigh_row][neigh_col] == 0 {
                res.push((neigh_row, neigh_col));
            }
        }
    }

    res
}

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        if grid[0][0] == 1 {
            return -1;
        }
        let mut heap: BinaryHeap<(Reverse<usize>, usize, usize)> = BinaryHeap::new();
        let mut visited = HashSet::new();
        let (rows, cols) = (grid.len(), grid[0].len());

        heap.push((Reverse(1), 0, 0));
        visited.insert((0, 0));

        while !heap.is_empty() {
            let (Reverse(distance), row, col) = heap.pop().unwrap();

            if (row, col) == (rows - 1, cols - 1) {
                return distance.try_into().unwrap();
            }

            for (neigh_row, neigh_col) in neighbours(&grid, row, col) {
                if visited.contains(&(neigh_row, neigh_col)) {
                    continue;
                }
                heap.push((Reverse(distance + 1), neigh_row, neigh_col));
                visited.insert((neigh_row, neigh_col));
            }
        }

        -1
    }
}
