#[allow(dead_code)]
struct Solution;

use std::collections::HashMap;

impl Solution {
    #[allow(dead_code)]
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut hash_map = HashMap::new();
        for num in nums {
            hash_map.entry(num).and_modify(|v| *v += 1).or_insert(1);
        }

        for v in hash_map.values() {
            if v % 2 != 0 {
                return false;
            }
        }
        true
    }
}
