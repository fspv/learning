class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        dp = [0 for _ in range(len(obstacleGrid[0]))]
        dp[0] = 1

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] != 1:
                    dp[col] += dp[col - 1] if col > 0 else 0
                else:
                    dp[col] = 0

        return dp[-1]
