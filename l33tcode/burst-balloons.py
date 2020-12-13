from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            max_coins = 0
            for burst in range(left + 1, right):
                max_coins = max(
                    max_coins,
                    dp(left, burst)
                    + dp(burst, right)
                    + nums[left] * nums[burst] * nums[right],
                )

            return max_coins

        nums = [1] + nums + [1]
        return dp(0, len(nums) - 1)


class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        nums_ext = [1] + nums + [1]

        dp = [[0] * (len(nums_ext) + 1) for _ in nums_ext]

        for left in reversed(range(1, len(nums_ext))):
            for right in range(left, len(nums_ext) + 1):
                for middle in range(left, right - 1):
                    burst_this = (
                        nums_ext[left - 1] * nums_ext[middle] * nums_ext[right - 1]
                    )
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][middle + 1] + dp[middle + 1][right] + burst_this,
                    )

        return dp[1][len(nums_ext)]

    def maxCoinsTopDown(self, nums: List[int]) -> int:
        nums_ext = [1] + nums + [1]

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            max_coins = 0
            for middle in range(left, right - 1):
                burst_this = nums_ext[left - 1] * nums_ext[middle] * nums_ext[right - 1]
                max_coins = max(
                    max_coins, dp(left, middle + 1) + dp(middle + 1, right) + burst_this
                )

            return max_coins

        return dp(1, len(nums_ext))
