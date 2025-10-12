#[allow(dead_code)]
struct Solution;

use std::collections::HashSet;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut map_a = HashSet::new();
        let mut map_b = HashSet::new();
        let mut count = 0;
        let mut res = Vec::new();

        for (i, val_a) in a.iter().enumerate() {
            let val_b = &b[i];

            if map_b.contains(val_a) {
                count += 1;
            }

            map_a.insert(val_a);

            if map_a.contains(val_b) {
                count += 1;
            }

            map_b.insert(val_b);

            res.push(count);
        }

        res
    }
}
