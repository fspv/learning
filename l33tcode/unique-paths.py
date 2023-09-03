class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = n, m

        dp = [0] * (cols + 1)
        # Can always get to the initial cell (row, cols > 0)
        dp[1] = 1

        for _ in range(rows):
            dp_old = dp
            dp = [0] * (cols + 1)
            for col in range(1, cols + 1):
                dp[col] = dp_old[col] + dp[col - 1]

        return dp[-1]
