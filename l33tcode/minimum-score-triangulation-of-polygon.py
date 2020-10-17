from typing import List
from functools import reduce, lru_cache


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[float("+inf")] * len(A) for _ in A]

        for start in reversed(range(len(A) - 1)):
            dp[start][start + 1] = 0
            for end in range(start + 2, len(A)):
                for middle in range(start + 1, end):
                    dp[start][end] = min(
                        dp[start][end],
                        A[start] * A[end] * A[middle]
                        + dp[start][middle]
                        + dp[middle][end],
                    )

        return dp[0][len(A) - 1]  # type: ignore

    def minScoreTriangulationTopDown(self, A: List[int]) -> int:
        @lru_cache(None)
        def dp(start: int, end: int) -> int:
            if start + 1 == end:
                return 0

            min_score = float("+inf")

            for middle in range(start + 1, end):
                min_score = min(
                    min_score,
                    A[start] * A[end] * A[middle] + dp(start, middle) + dp(middle, end),
                )

            return min_score  # type: ignore

        return dp(0, len(A) - 1)  # type: ignore
