#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut nums_copy = nums.clone();

        let mut left: usize = 0;
        let mut right: usize = nums.len() - 1;

        for &num in nums.iter().filter(|&&num| num < pivot) {
            nums_copy[left] = num;
            left += 1;
        }

        for &num in nums.iter().rev().filter(|&&num| num > pivot) {
            nums_copy[right] = num;
            right -= 1;
        }

        (left..=right).for_each(|i| {
            nums_copy[i] = pivot;
        });

        nums_copy
    }
}
