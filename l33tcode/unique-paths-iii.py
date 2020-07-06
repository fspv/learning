from typing import List
from functools import lru_cache


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        start_row, start_col = -1, -1
        empty = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    start_row, start_col = row, col
                elif grid[row][col] == 0:
                    empty += 1

        def neighbors(row, col):
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    yield (neigh_row, neigh_col)

        visited = set()

        def dfs(row, col):
            if grid[row][col] == 2:
                return int(len(visited) - 1 == empty)

            if grid[row][col] == -1:
                return 0

            ways = 0

            visited.add((row, col))
            for neigh_row, neigh_col in neighbors(row, col):
                if (neigh_row, neigh_col) not in visited:
                    ways += dfs(neigh_row, neigh_col)
            visited.remove((row, col))

            return ways

        return dfs(start_row, start_col)
