#[allow(dead_code)]
pub struct Solution;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn has_increasing_subarrays(nums: Vec<i32>, k: i32) -> bool {
        let mut found = k == 1; // prev subarray has len k
        let mut count = 1;

        for i in 1..nums.len() {
            if nums[i - 1] < nums[i] {
                count += 1;
                if count >= k * 2 {
                    return true;
                }

                if count >= k && found {
                    return true;
                }

                continue;
            }

            if count >= k {
                if found {
                    return true;
                }
                found = true;
            } else {
                found = false;
            }
            count = 1;
        }
        false
    }
}
