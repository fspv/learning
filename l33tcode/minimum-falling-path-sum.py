from functools import lru_cache


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(row: int, prev_col: int) -> int:
            if row == len(A):
                return 0

            min_sum = float("+inf")

            for col in filter(
                lambda x: x >= 0 and x < len(A), [prev_col - 1, prev_col, prev_col + 1]
            ):
                min_sum = min(min_sum, dp(row + 1, col) + A[row][col])

            return min_sum

        if not A:
            return 0

        min_sum = float("+inf")

        for col in range(len(A[0])):
            min_sum = min(min_sum, dp(0, col))

        return min_sum
