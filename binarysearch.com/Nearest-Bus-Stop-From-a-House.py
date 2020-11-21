from enum import Enum
from typing import List, Iterator, Set, Tuple, Deque, DefaultDict
from collections import deque, defaultdict


class CellType(Enum):
    EMPTY = 0
    WALL = 1
    HOUSE = 2
    BUS_STOP = 3


class Solution:
    def solve(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        def neighbors(
            row: int, col: int, visited: Set[Tuple[int, int]]
        ) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and (neigh_row, neigh_col) not in visited
                    and matrix[neigh_row][neigh_col]
                    not in {CellType.WALL.value, CellType.HOUSE.value}
                ):
                    yield (neigh_row, neigh_col)

        def bfs() -> int:
            queue: Deque[Tuple[int, int, int]] = deque()

            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col] == CellType.HOUSE.value:
                        queue.append((0, row, col))

            visited: Set[Tuple[int, int]] = set()

            while queue:
                distance, row, col = queue.popleft()
                visited.add((row, col))

                if matrix[row][col] == CellType.BUS_STOP.value:
                    return distance

                for neigh_row, neigh_col in neighbors(row, col, visited):
                    queue.append((distance + 1, neigh_row, neigh_col))

            return -1

        return bfs()
