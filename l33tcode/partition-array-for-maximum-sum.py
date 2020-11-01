from typing import List, Tuple
from functools import lru_cache


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for start in range(len(arr)):
            max_val = 0
            for end in range(start + 1, min(len(arr) + 1, start + k + 1)):
                max_val = max(max_val, arr[end - 1])
                dp[end] = max(dp[start] + max_val * (end - start), dp[end],)

        return dp[-1]

    def maxSumAfterPartitioningTopDown(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(start: int, end: int) -> Tuple[int, int]:
            max_total = arr[start]
            max_val = arr[start]

            for middle in range(start + 1, min(end, start + k + 1)):
                max_left, total_left = dp(start, middle)
                max_right, total_right = dp(middle, end)

                max_total = max(max_total, total_left + total_right)
                max_val = max(max_left, max_right)

            if end - start <= k:
                max_total = max(max_total, max_val * (end - start))

            return max_val, max_total

        return dp(0, len(arr))[1]
