from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        partial_sums = list(accumulate(nums, initial=0))

        dp = [[0] * len(nums) for _ in nums]

        for left in reversed(range(len(nums))):
            dp[left][left] = nums[left]

            for right in range(left + 1, len(nums)):
                partial_sum = partial_sums[right + 1] - partial_sums[left]

                dp[left][right] = partial_sum - min(
                    dp[left][right - 1], dp[left + 1][right]
                )

        score = dp[0][len(nums) - 1]
        return score >= partial_sums[-1] - score

    def PredictTheWinnerTopDown(self, nums: List[int]) -> bool:
        partial_sums = list(accumulate(nums, initial=0))

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            partial_sum = partial_sums[right + 1] - partial_sums[left]

            return partial_sum - min(dp(left, right - 1), dp(left + 1, right))

        score = dp(0, len(nums) - 1)
        return score >= partial_sums[-1] - score

