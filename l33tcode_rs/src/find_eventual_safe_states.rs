#[allow(dead_code)]
struct Solution;

use std::collections::VecDeque;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let mut inverse_graph_indegrees = vec![0; graph.len()];
        let mut inverse_graph = vec![vec![]; graph.len()];

        for (src, dsts) in graph.iter().enumerate() {
            for dst in dsts.iter().map(|d| usize::try_from(*d).unwrap()) {
                inverse_graph_indegrees[src] += 1;
                inverse_graph[dst].push(i32::try_from(src).unwrap());
            }
        }

        let mut queue = VecDeque::new();

        for node in inverse_graph_indegrees
            .iter()
            .enumerate()
            .filter(|(_, c)| **c == 0)
            .map(|(c, _)| c)
        {
            queue.push_back(node);
        }

        let mut res = Vec::new();

        while let Some(node) = queue.pop_front() {
            res.push(i32::try_from(node).unwrap());
            for next_node in inverse_graph[node].as_slice() {
                let next_node_usize = usize::try_from(*next_node).unwrap();
                inverse_graph_indegrees[next_node_usize] -= 1;

                if inverse_graph_indegrees[next_node_usize] == 0 {
                    queue.push_back(next_node_usize);
                }
            }
        }

        // Can avoid this with bucket sort, but this doesn't affect the overall complexity
        res.sort_unstable();

        res
    }
}
