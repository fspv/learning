from typing import List


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        rows, cols = len(M), len(M[0]) if M else 0
        dp = [[(0, 0, 0, 0)] * (cols + 2) for _ in range(rows + 2)]

        result = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if M[row - 1][col - 1] == 1:
                    dp[row][col] = (
                        dp[row - 1][col - 1][0] + 1,
                        dp[row][col - 1][1] + 1,
                        dp[row - 1][col][2] + 1,
                        dp[row - 1][col + 1][3] + 1,
                    )

                    result = max(result, max(dp[row][col]))

        return result
