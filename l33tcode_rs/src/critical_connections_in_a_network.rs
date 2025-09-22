#[allow(dead_code)]
pub struct Solution;

use std::cmp::min;

#[derive(Debug, Default)]
struct DfsState {
    low_times: Vec<usize>,
    times: Vec<usize>,
    visited: Vec<bool>,
    adj_list: Vec<Vec<usize>>,
    result: Vec<Vec<i32>>,
}

impl Solution {
    #[allow(dead_code)]
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut adj_list: Vec<Vec<usize>> = vec![Vec::new(); n.try_into().unwrap()];

        for connection in connections {
            let src: usize = connection[0].try_into().unwrap();
            let dst: usize = connection[1].try_into().unwrap();
            adj_list[src].push(dst);
            adj_list[dst].push(src);
        }

        let mut state = DfsState {
            low_times: vec![0; n.try_into().unwrap()],
            times: vec![0; n.try_into().unwrap()],
            visited: vec![false; n.try_into().unwrap()],
            adj_list,
            result: Vec::new(),
        };

        for pos in 0..n.try_into().unwrap() {
            if !state.visited[pos] {
                state.visited[pos] = true;
                Self::dfs(pos, usize::MAX, &mut 0, &mut state);
            }
        }

        state.result
    }

    fn dfs(node: usize, parent: usize, time: &mut usize, state: &mut DfsState) -> usize {
        state.times[node] = *time;
        state.low_times[node] = *time;

        let neighbors = state.adj_list[node].clone();
        for &neigh_pos in &neighbors {
            if !state.visited[neigh_pos] {
                state.visited[neigh_pos] = true;
                *time += 1;
                *time = Self::dfs(neigh_pos, node, time, state);
            }

            if neigh_pos != parent {
                state.low_times[node] = min(state.low_times[node], state.low_times[neigh_pos]);
            }
        }

        if state.times[node] <= state.low_times[node] && parent != usize::MAX {
            state.result.push(vec![
                i32::try_from(node).unwrap(),
                i32::try_from(parent).unwrap(),
            ]);
        }

        *time
    }
}
