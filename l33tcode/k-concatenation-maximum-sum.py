from typing import List
from functools import lru_cache


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        max_sum = 0
        dp = 0

        for _ in range(2):
            for pos in range(len(arr)):
                dp = max(dp + arr[pos], 0)
                max_sum = max(max_sum, dp)

        total = sum(arr)

        if total > 0:
            max_sum = total * (k - 2) + max_sum

        return max_sum % MOD

    def kConcatenationMaxSumTopDown(self, arr: List[int], k: int) -> int:
        max_sum = 0

        @lru_cache(None)
        def dp(pos: int, repeats: int) -> int:
            nonlocal max_sum

            if repeats == 2:
                return 0

            next_pos = (pos + 1) % len(arr)
            next_repeats = repeats + (pos + 1) // len(arr)

            max_next = dp(next_pos, next_repeats)

            if max_next + arr[pos] >= 0:
                max_sum = max(max_sum, max_next + arr[pos])
                return max_next + arr[pos]
            else:
                return 0

        dp(0, 0)

        return max_sum
