class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        visited = set()

        def neighbours(row, col):
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                yield neigh_row, neigh_col

        def dfs(row, col):
            if grid[row][col] == 0:
                return 1

            perimeter = 0

            visited.add((row, col))
            for neigh_row, neigh_col in neighbours(row, col):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    if (neigh_row, neigh_col) not in visited:
                        perimeter += dfs(neigh_row, neigh_col)
                else:
                    perimeter += 1

            return perimeter

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)

        return 0
