#[allow(dead_code)]
struct Solution;

use std::collections::HashSet;

impl Solution {
    #[allow(dead_code)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut set = HashSet::new();
        let mut unique_len = 0;

        for (i, num) in nums.iter().enumerate().rev() {
            if !set.insert(num) {
                break;
            }
            unique_len = i;
        }

        (unique_len / 3 + usize::from(unique_len % 3 > 0))
            .try_into()
            .unwrap()
    }
}
