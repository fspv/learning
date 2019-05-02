class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[1][0] = 1

        for row in range(n):
            for col in range(m):
                dp[row + 1][col + 1] = dp[row][col + 1] + dp[row + 1][col]

        return dp[n][m]
