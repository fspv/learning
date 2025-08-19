#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut zeroes = 0;
        let mut result = 0;

        for num in &nums {
            if *num == 0 {
                zeroes += 1;
            } else {
                result += (zeroes + 1) * zeroes / 2;
                zeroes = 0;
            }
        }

        result += (zeroes + 1) * zeroes / 2;

        result
    }
}
