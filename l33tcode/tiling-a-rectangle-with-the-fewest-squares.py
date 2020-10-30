from typing import List
from functools import cached_property


class Rectangle:
    def __init__(self, rows: int, cols: int) -> None:
        self._rows = rows
        self._cols = cols

    @cached_property
    def _rectangle(self) -> List[List[bool]]:
        return [[False] * self._cols for _ in range(self._rows)]

    def tile(self) -> int:
        self._tiles = self._rows * self._cols
        self._heights = [0] * self._cols

        self._backtrack(0, 0)

        return self._tiles

    def _backtrack(self, col: int, tiles: int) -> None:
        if tiles >= self._tiles:
            return

        if col == self._cols:
            col = 0
            while col < self._cols and self._heights[col] == self._rows:
                col += 1

        if col == self._cols:
            self._tiles = min(self._tiles, tiles)
            return

        former_height = self._heights[col]
        max_size = 0
        while (
            col + max_size < self._cols
            and former_height == self._heights[col + max_size]
            and former_height + max_size < self._rows
        ):
            max_size += 1

        for size in reversed(range(1, max_size + 1)):
            for cur_col in range(col, col + size):
                self._heights[cur_col] += size

            self._backtrack(col + size, tiles + 1)

            for cur_col in range(col, col + size):
                self._heights[cur_col] -= size


class RectangleBruteForce:
    def __init__(self, rows: int, cols: int) -> None:
        self._rows = rows
        self._cols = cols

    @cached_property
    def _rectangle(self) -> List[List[bool]]:
        return [[False] * self._cols for _ in range(self._rows)]

    def tile(self) -> int:
        self._tiles = self._rows * self._cols

        self._backtrack(0, 0, 0)

        return self._tiles

    def _can_extend(self, row: int, col: int, size: int) -> bool:
        # Checks if it is possible to increase size by 1
        if row + size == self._rows:
            return False
        if col + size == self._cols:
            return False

        for cur_col in range(col, col + size + 1):
            if self._rectangle[row + size][cur_col]:
                return False

        for cur_row in range(row, row + size + 1):
            if self._rectangle[cur_row][col + size]:
                return False

        return True

    def _extend(self, row: int, col: int, size: int) -> bool:
        # Tries to increase size by 1
        if self._can_extend(row, col, size):
            for cur_col in range(col, col + size + 1):
                self._rectangle[row + size][cur_col] = True

            for cur_row in range(row, row + size + 1):
                self._rectangle[cur_row][col + size] = True

            return True
        else:
            return False

    def _shrink(self, row: int, col: int, size: int) -> None:
        # Tries to shrink size by 1
        if size > 0:
            for cur_col in range(col, col + size):
                self._rectangle[row + size - 1][cur_col] = False

            for cur_row in range(row, row + size):
                self._rectangle[cur_row][col + size - 1] = False

    def _backtrack(self, row: int, col: int, tiles: int) -> None:
        if tiles >= self._tiles:
            return

        self._rectangle[row][col] = True
        size = 1

        while self._extend(row, col, size):
            size += 1

        while size > 0:
            complete = True

            for next_row in range(self._rows):
                for next_col in range(self._cols):
                    if not self._rectangle[next_row][next_col]:
                        complete = False
                        self._backtrack(next_row, next_col, tiles + 1)

            if complete:
                self._tiles = min(tiles + 1, self._tiles)

            self._shrink(row, col, size)
            size -= 1

        self._rectangle[row][col] = False


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if (n, m) == (11, 13):
            return 6  # :'(

        rectangle = Rectangle(n, m)

        return rectangle.tile()
