class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        max_dp = sum(sum(r) for r in grid)
        dp = [[max_dp] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for row in range(rows):
            for col in range(cols):
                if 0 <= col - 1:
                    dp[row][col] = min(dp[row][col], grid[row][col] + dp[row][col - 1])
                if 0 <= row - 1:
                    dp[row][col] = min(dp[row][col], grid[row][col] + dp[row - 1][col])

        return dp[-1][-1]

    def minPathSum2(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        stack = set([(rows - 1, cols - 1)])
        dp = [[None] * cols for row in range(rows)]
        dp[rows - 1][cols - 1] = 0

        while stack:
            old_stack = stack
            stack = set()

            for row, col in old_stack:
                dp[row][col] = float("+inf")
                dp[row][col] = min(
                    (
                        grid[row + 1][col] + dp[row + 1][col]
                        if row + 1 < len(grid)
                        else float("+inf")
                    ),
                    (
                        grid[row][col + 1] + dp[row][col + 1]
                        if col + 1 < len(grid[0])
                        else float("+inf")
                    ),
                )
                dp[row][col] = 0 if dp[row][col] == float("+inf") else dp[row][col]
                if row - 1 >= 0:
                    stack.add((row - 1, col))
                if col - 1 >= 0:
                    stack.add((row, col - 1))

        return dp[0][0] + grid[0][0]
