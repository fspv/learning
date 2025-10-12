#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        const MIN: i32 = -10i32.pow(6) - 1;
        const MAX: i32 = 10i32.pow(6) + 1;
        let mut nums_larger = &nums1;
        let mut nums_smaller = &nums2;
        if nums1.len() < nums2.len() {
            nums_larger = &nums2;
            nums_smaller = &nums1;
        }
        let (mut left, mut right) = (0, nums_smaller.len());

        let median = (nums_smaller.len() + nums_larger.len()).div_ceil(2);

        while left <= right {
            let mid_smaller = left + (right - left) / 2;
            let mid_larger = median - mid_smaller;

            let larger_before = nums_larger.get(mid_larger - 1).unwrap_or(&MIN);
            let larger_after = nums_larger.get(mid_larger).unwrap_or(&MAX);

            let smaller_before = nums_smaller.get(mid_smaller - 1).unwrap_or(&MIN);
            let smaller_after = nums_smaller.get(mid_smaller).unwrap_or(&MAX);

            if larger_before <= smaller_after && smaller_before <= larger_after {
                if (nums_larger.len() + nums_smaller.len()) % 2 == 0 {
                    return f64::from(
                        larger_before.max(smaller_before) + larger_after.min(smaller_after),
                    ) / 2.0;
                }
                return f64::from(*larger_before.max(smaller_before));
            } else if smaller_before > larger_after {
                right = mid_smaller;
            } else {
                left = mid_smaller + 1;
            }
        }

        panic!("Median doesn't exist")
    }
}
