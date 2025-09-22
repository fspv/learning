#[allow(dead_code)]
pub struct Solution;

use std::collections::HashMap;

impl Solution {
    #[allow(dead_code)]
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();

        for num in nums {
            *freq.entry(num).or_insert(0) += 1;
        }

        let max_freq = freq.values().max().unwrap();

        (freq.values().filter(|f| *f == max_freq).count() * max_freq).try_into().unwrap()
    }
}
