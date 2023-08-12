from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacles: List[List[int]]) -> int:
        rows, cols = len(obstacles), len(obstacles[0]) if obstacles else 0

        # We don't need to store data for all the previous rows, becauce we
        # only look the `row - 1`
        dp = [0] * cols
        dp[0] = 1

        for row in range(rows):
            for col in range(cols):
                if obstacles[row][col]:
                    dp[col] = 0
                else:
                    dp[col] += dp[col - 1] if col > 0 else 0

        return dp[-1]
