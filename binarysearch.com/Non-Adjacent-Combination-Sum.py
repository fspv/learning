from typing import List
from functools import lru_cache


class Solution:
    def solve(self, nums: List[int], k: int) -> bool:
        dp = [
            {0} for _ in range(len(nums) + 2)
        ]

        for pos in range(len(nums)):
            for num in dp[pos]:
                dp[pos + 2].add(num + nums[pos])
                dp[pos + 1].add(num)

                if k in {num, num + nums[pos]}:
                    return True

        return False

    def solveTopDown(self, nums: List[int], k: int) -> bool:
        @lru_cache(None)
        def dp(pos: int, left: int) -> bool:
            if left == 0:
                return True

            if pos >= len(nums):
                return False

            if left < 0:
                return False

            return dp(pos + 2, left - nums[pos]) or dp(pos + 1, left)

        return dp(0, k)

    def solveBruteForce(self, nums: List[int], k: int) -> bool:
        dp = [{0, num} for num in nums]
        for left_pos in range(len(nums)):
            if k in dp[left_pos]:
                return True

            for right_pos in range(left_pos + 2, len(nums)):
                for num in dp[left_pos]:
                    dp[right_pos].add(num + nums[right_pos])

        return False
