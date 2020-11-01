from typing import List
from functools import lru_cache


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True

        partial_sums = [0]
        for num in nums:
            partial_sums.append(partial_sums[-1] + num)

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            return max(
                (partial_sums[right] - partial_sums[left] - dp(left, right - 1))
                + nums[right],
                (partial_sums[right + 1] - partial_sums[left + 1] - dp(left + 1, right))
                + nums[left],
            )

        max_score = dp(0, len(nums) - 1)

        return max_score >= (partial_sums[-1] - max_score)
