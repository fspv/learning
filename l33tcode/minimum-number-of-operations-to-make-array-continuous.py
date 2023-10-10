from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_len = len(nums)
        nums = sorted(set(nums))

        min_ops = total_len

        right = 0

        for left in range(len(nums)):
            while right < len(nums) and nums[right] < nums[left] + total_len:
                right += 1

            min_ops = min(min_ops, total_len - (right - left))

        return min_ops
