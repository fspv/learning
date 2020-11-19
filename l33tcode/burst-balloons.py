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
