impl Solution {
    pub fn minimize_max(nums: Vec<i32>, p: i32) -> i32 {
        let mut nums = nums;
        nums.sort();

        fn pairs_exist(nums: &Vec<i32>, max_diff: i32, pairs: i32) -> bool {
            let mut count = 0;
            let mut pos = 1;

            while pos < nums.len() {
                if nums[pos] - nums[pos - 1] <= max_diff {
                    count += 1;
                    pos += 1;
                }

                pos += 1;
            }

            return count >= pairs;
        }

        let mut left = 0;
        let mut right = nums[nums.len() - 1] - nums[0];

        while left < right {
            let mid = left + (right - left) / 2;

            if !pairs_exist(&nums, mid, p) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
