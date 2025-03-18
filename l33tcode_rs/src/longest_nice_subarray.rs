struct Solution;

use std::cmp::max;

impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let mut left: usize = 0;
        let mut ans: i32 = 0;
        // All the elements should have distinct bits set to 1 in order
        // for AND of all of the pairs to be 0. This value is set to OR
        // of all of the nums in the latest successfully detected nice array
        let mut buf: i32 = 0;

        for (right, num) in nums.iter().enumerate() {
            while (buf & num) != 0 {
                buf ^= nums[left];
                left += 1;
            }

            buf |= num;

            ans = max(ans, (right - left + 1).try_into().unwrap());
        }

        ans
    }
}
