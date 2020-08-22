from typing import List, Iterator, Tuple


class Color:
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        colors = [[Color.WHITE] * cols for _ in range(rows)]

        def neighbours(
            row: int, col: int, prev_row: int, prev_col: int
        ) -> Iterator[Tuple[int, int]]:
            rows, cols = len(grid), len(grid[0]) if grid else 0
            for neigh_row, neigh_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and (neigh_row, neigh_col) != (prev_row, prev_col)
                    and grid[row][col] == grid[neigh_row][neigh_col]
                ):
                    yield neigh_row, neigh_col

        def dfs(row: int, col: int, prev_row: int, prev_col: int) -> bool:
            # True - we have cycles, False - we don't
            if colors[row][col] == Color.GRAY:
                return True

            if colors[row][col] == Color.BLACK:
                return False

            colors[row][col] = Color.GRAY

            for neigh_row, neigh_col in neighbours(row, col, prev_row, prev_col):
                if dfs(neigh_row, neigh_col, row, col):
                    return True

            colors[row][col] = Color.BLACK
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, -1, -1):
                    return True

        return False
