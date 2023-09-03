class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = n, m

        if rows == 0 or cols == 0:
            return 0

        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        dp[1][0] = 1

        for row in range(rows):
            for col in range(cols):
                dp[row + 1][col + 1] = dp[row][col + 1] + dp[row + 1][col]

        return dp[rows][cols]
