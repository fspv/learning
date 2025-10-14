#[allow(dead_code)]
struct Solution;

use std::collections::HashMap;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            if let Some(pos) = map.get(&(target - num)) {
                return vec![*pos, i.try_into().unwrap()];
            }

            map.insert(*num, i.try_into().unwrap());
        }

        vec![]
    }
}
