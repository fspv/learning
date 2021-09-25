from collections import deque
from typing import Deque, Iterator, List, Tuple


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        # distance, row, col, eliminations left
        queue: Deque[Tuple[int, int, int, int]] = deque([(0, 0, 0, k)])
        visited: List[List[int]] = [[rows * cols] * cols for _ in range(rows)]
        visited_left: List[List[int]] = [[0] * cols for _ in range(rows)]

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row, col - 1),
                (row + 1, col),
                (row, col + 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    yield neigh_row, neigh_col

        while queue:
            distance, row, col, left = queue.popleft()

            if (row, col) == (rows - 1, cols - 1):
                return distance

            for neigh_row, neigh_col in neighbors(row, col):
                if grid[neigh_row][neigh_col] == 1:
                    # Eliminate obstacle if possible
                    if visited_left[neigh_row][neigh_col] > left - 1:
                        continue

                    if (
                        visited_left[neigh_row][neigh_col] == left - 1
                        and visited[neigh_row][neigh_col] <= distance + 1
                    ):
                        continue

                    if left > 0:
                        visited[neigh_row][neigh_col] = distance + 1
                        visited_left[neigh_row][neigh_col] = left - 1
                        queue.append((distance + 1, neigh_row, neigh_col, left - 1))
                else:
                    # Just proceed further
                    if visited_left[neigh_row][neigh_col] > left:
                        continue

                    if (
                        visited_left[neigh_row][neigh_col] == left
                        and visited[neigh_row][neigh_col] <= distance + 1
                    ):
                        continue

                    visited[neigh_row][neigh_col] = distance + 1
                    visited_left[neigh_row][neigh_col] = left
                    queue.append((distance + 1, neigh_row, neigh_col, left))

        return -1
