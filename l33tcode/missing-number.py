from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        for num in range(len(nums) + 1):
            xor ^= num

        return xor
