from functools import cache
from typing import List, Tuple


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        @cache
        def dp(pos: int) -> Tuple[int, int]:
            """
            returns (negative, positive)
            """
            if pos == len(nums):
                return (0, 0)

            if nums[pos] == 0:
                return (0, 0)

            negative, positive = dp(pos + 1)

            if nums[pos] > 0:
                return (negative + 1 if negative > 0 else 0, positive + 1)
            elif nums[pos] < 0:
                return (positive + 1, negative + 1 if negative > 0 else 0)

        max_len = 0
        for pos in range(len(nums)):
            max_len = max(max_len, dp(pos)[1])

        return max_len
