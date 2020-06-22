class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])

        dp = [[0] * cols for _ in range(rows)]

        def neighbours(row, col):
            for neigh_row, neigh_col in [
                (row + 1, col),
                (row, col + 1),
            ]:
                if neigh_row < rows and neigh_col < cols:
                    yield neigh_row, neigh_col

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                dp[row][col] = min(
                    (
                        dp[neigh_row][neigh_col]
                        for neigh_row, neigh_col in neighbours(row, col)
                    ),
                    default=1,
                )
                dp[row][col] = max(dp[row][col] - dungeon[row][col], 1)

        return dp[0][0]
