#[allow(dead_code)]
pub struct Solution;

use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    #[allow(dead_code)]
    pub fn can_measure_water(x: i32, y: i32, target: i32) -> bool {
        let (x_max, y_max) = (x, y);

        let mut q = VecDeque::new();
        let mut visited = HashSet::new();

        q.push_back((x, y));
        visited.insert((x, y));

        while let Some((x, y)) = q.pop_front() {
            if x + y == target {
                return true;
            }

            for (next_x, next_y) in [
                (0, y),
                (x, 0),
                (x_max, y),
                (x, y_max),
                (x_max.min(x + y), 0.max(x + y - x_max)),
                (0.max(x + y - y_max), y_max.min(x + y)),
            ] {
                if visited.contains(&(next_x, next_y)) {
                    continue;
                }
                visited.insert((next_x, next_y));
                q.push_back((next_x, next_y));
            }
        }

        false
    }
}
