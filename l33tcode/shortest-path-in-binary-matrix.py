import heapq
from typing import List, Tuple, Iterator, Union


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row, col - 1),
                (row + 1, col),
                (row, col + 1),
                (row - 1, col - 1),
                (row + 1, col + 1),
                (row - 1, col + 1),
                (row + 1, col - 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and grid[neigh_row][neigh_col] == 0
                ):
                    yield neigh_row, neigh_col

        def distance_squared(row1: int, col1: int, row2: int, col2: int) -> int:
            return (row1 - row2) ** 2 + (col1 - col2) ** 2

        heap: List[Tuple[int, int, int, int]] = []
        distances: List[List[Union[float, int]]] = [
            [float("+inf")] * cols for _ in range(rows)
        ]

        if grid[0][0] == 0:
            heapq.heappush(heap, (0, 0, 0, distance_squared(rows - 1, cols - 1, 0, 0)))

        while heap:
            row, col, distance, _ = heapq.heappop(heap)

            if (row, col) == (rows - 1, cols - 1):
                return distance + 1

            if distance >= distances[row][col]:
                continue

            distances[row][col] = distance

            for neigh_row, neigh_col in neighbors(row, col):
                heapq.heappush(
                    heap,
                    (
                        neigh_row,
                        neigh_col,
                        distance + 1,
                        distance_squared(rows - 1, cols - 1, row, col),
                    ),
                )

        return -1
