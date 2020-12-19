from typing import List, Iterator, Tuple
from functools import lru_cache


class Grid:
    def __init__(self, grid: List[List[int]]) -> None:
        self._grid = grid
        self._rows = len(grid)
        self._cols = len(grid[0]) if grid else 0

    def _neighbors(self, row: int, col: int) -> Iterator[Tuple[int, int]]:
        for neigh_row, neigh_col in (
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ):
            if neigh_row < self._rows and 0 <= neigh_col < self._cols:
                yield (neigh_row, neigh_col)

    @lru_cache(None)
    def _dp(self, row: int, col1: int, col2: int) -> int:
        cherries = (
            self._grid[row][col1] + self._grid[row][col2]
            if col1 != col2
            else self._grid[row][col1]
        )

        max_cherries = cherries

        for neigh_row1, neigh_col1 in self._neighbors(row, col1):
            for neigh_row2, neigh_col2 in self._neighbors(row, col2):
                max_cherries = max(
                    max_cherries,
                    cherries + self._dp(neigh_row1, neigh_col1, neigh_col2),
                )

        return max_cherries

    def _dp_bottom_up(self) -> int:
        dp = [[0] * self._cols for _ in range(self._cols)]

        for row in reversed(range(self._rows)):
            dp_old = dp
            dp = [[0] * self._cols for _ in range(self._cols)]

            for col1 in range(self._cols):
                for col2 in range(self._cols):
                    cherries = (
                        self._grid[row][col1] + self._grid[row][col2]
                        if col1 != col2
                        else self._grid[row][col1]
                    )
                    dp[col1][col2] = cherries

                    for _, neigh_col1 in self._neighbors(row, col1):
                        for _, neigh_col2 in self._neighbors(row, col2):
                            dp[col1][col2] = max(
                                dp[col1][col2],
                                cherries + dp_old[neigh_col1][neigh_col2],
                            )

        return dp[0][self._cols - 1]

    def max_cherries(self) -> int:
        # return self._dp(0, 0, self._cols - 1)
        return self._dp_bottom_up()


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        return Grid(grid).max_cherries()
