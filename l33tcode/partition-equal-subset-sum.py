from typing import List
from functools import lru_cache


class Solution:
    def canPartitionTopDown(self, nums: List[int]) -> bool:
        total = sum(nums)

        @lru_cache(None)
        def knapsack(capacity: int, pos: int) -> bool:
            if pos >= len(nums):
                return False

            if capacity > total / 2:
                return False

            if capacity == total / 2:
                return True

            pick_this = knapsack(capacity + nums[pos], pos + 1)
            skip_this = knapsack(capacity, pos + 1)

            return pick_this or skip_this

        return knapsack(0, 0)

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total / 2

        dp = []

        for pos in range(len(nums)):
            dp.append([False] * int(half + 1))
            dp[pos][0] = True
            for capacity in range(1, int(half + 1)):
                if pos == 0:
                    dp[pos][capacity] = capacity == nums[pos]
                    continue

                dp[pos][capacity] = dp[pos - 1][capacity]

                if capacity >= nums[pos]:
                    dp[pos][capacity] = dp[pos][capacity] or dp[pos - 1][capacity - nums[pos]]

                if capacity == half and dp[pos][capacity]:
                    return True

        return False

    def canPartition2(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(pos: int, left: int) -> bool:
            if left == 0:
                return True

            if pos == len(nums):
                return False

            if dp(pos + 1, left):
                return True

            if nums[pos] <= left and dp(pos + 1, left - nums[pos]):
                return True

            return False

        total = sum(nums)

        if total % 2 != 0:
            return False

        return dp(0, total / 2)
