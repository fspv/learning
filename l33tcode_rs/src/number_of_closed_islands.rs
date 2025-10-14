#[allow(dead_code)]
struct Solution;

use std::collections::HashSet;

struct UnionFind {
    roots: Vec<Vec<(usize, usize)>>,
    counts: Vec<Vec<usize>>,
}

impl UnionFind {
    fn new(rows: usize, cols: usize) -> Self {
        UnionFind {
            roots: (0..rows)
                .map(|row| (0..cols).map(|col| (row, col)).collect())
                .collect(),
            counts: vec![vec![1; cols]; rows],
        }
    }

    fn union(&mut self, row1: usize, col1: usize, row2: usize, col2: usize) {
        let (mut row_less, mut col_less, mut row_more, mut col_more) = (row1, col1, row2, col2);

        if self.counts[row_less][col_less] > self.counts[row_more][col_more] {
            (row_less, col_less, row_more, col_more) = (row_more, col_more, row_less, col_less);
        }

        self.roots[row_less][col_less] = self.roots[row_more][col_more];
        self.counts[row_more][col_more] += self.counts[row_less][col_less];
    }

    fn find(&mut self, row: usize, col: usize) -> (usize, usize) {
        let (root_row, root_col) = self.roots[row][col];

        if (root_row, root_col) == (row, col) {
            return (root_row, root_col);
        }

        self.roots[row][col] = self.find(root_row, root_col);

        self.roots[row][col]
    }
}

fn neighbours(grid: &[Vec<i32>], row: usize, col: usize) -> Vec<(usize, usize)> {
    let (rows, cols) = (grid.len(), grid[0].len());

    let mut res = vec![];
    for (neigh_row_opt, neigh_col_opt) in [
        (row.checked_sub(1), Some(col)),
        (Some(row), col.checked_sub(1)),
        (Some(row), Some(col + 1)),
        (Some(row + 1), Some(col)),
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
    pub fn closed_island(grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }

        let (rows, cols) = (grid.len(), grid[0].len());

        let mut union_find = UnionFind::new(rows, cols);

        for row in 0..rows {
            for col in 0..cols {
                if grid[row][col] != 0 {
                    continue;
                }
                for (neigh_row, neigh_col) in neighbours(&grid, row, col) {
                    let (root1_row, root1_col) = union_find.find(row, col);
                    let (root2_row, root2_col) = union_find.find(neigh_row, neigh_col);
                    if (root1_row, root1_col) != (root2_row, root2_col) {
                        union_find.union(root1_row, root1_col, root2_row, root2_col);
                    }
                }
            }
        }

        let mut set = HashSet::new();

        #[allow(clippy::needless_range_loop)]
        for row in 0..rows {
            for col in 0..cols {
                if grid[row][col] != 0 {
                    continue;
                }
                let root = union_find.find(row, col);
                set.insert(root);
            }
        }

        #[allow(clippy::needless_range_loop)]
        for row in 0..rows {
            for col in 0..cols {
                if grid[row][col] != 0 {
                    continue;
                }
                if row == 0 || row == rows - 1 || col == 0 || col == cols - 1 {
                    let root = union_find.find(row, col);
                    set.remove(&root);
                }
            }
        }

        set.len().try_into().unwrap()
    }
}
