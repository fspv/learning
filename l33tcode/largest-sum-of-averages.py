from typing import List
from functools import lru_cache


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        @lru_cache(None)
        def dp(start: int, partitions: int) -> float:
            if start == len(A):
                if partitions == 0:
                    return 0.0
                else:
                    return float("-inf")

            if partitions == 0:
                return float("-inf")

            average = 0.0
            max_average = 0.0

            for end in range(start + 1, len(A) + 1):
                average = (average * (end - start - 1) + A[end - 1]) / (end - start)
                max_average = max(max_average, dp(end, partitions - 1) + average)

            return max_average

        return dp(0, K)
