from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def condition(subarray_sum: int) -> bool:
            # we canot construct m subarrays -> False
            # else -> True

            cur_sum = 0
            pos = 0
            count = 1

            while pos < len(nums):
                if cur_sum > subarray_sum:
                    return True

                if cur_sum + nums[pos] > subarray_sum:
                    cur_sum = nums[pos]
                    count += 1
                else:
                    cur_sum += nums[pos]

                if count > m:
                    return True

                pos += 1

            return False

        left, right = max(nums), sum(nums)

        while left < right:
            middle = left + (right - left) // 2

            if condition(middle):
                left = middle + 1
            else:
                right = middle

        return left
