from collections import deque
from typing import Deque, Iterator, List, Tuple


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        sum_distance: List[List[int]] = [[0] * cols for _ in range(rows)]
        houses_reachable: List[List[int]] = [[0] * cols for _ in range(rows)]

        def neighbors(
            row: int, col: int, visited: List[List[bool]]
        ) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    if (
                        grid[neigh_row][neigh_col] != 2
                        and grid[neigh_row][neigh_col] != 1
                        and not visited[neigh_row][neigh_col]
                    ):
                        yield neigh_row, neigh_col

        def bfs(start_row: int, start_col: int) -> None:
            visited: List[List[bool]] = [[False] * cols for _ in range(rows)]
            queue: Deque[Tuple[int, int, int]] = deque(
                [(0, start_row, start_col)]
            )  # distance, row, col
            visited[start_row][start_col] = True

            while queue:
                distance, row, col = queue.popleft()

                sum_distance[row][col] += distance
                houses_reachable[row][col] += 1

                for neigh_row, neigh_col in neighbors(row, col, visited):
                    visited[neigh_row][neigh_col] = True
                    queue.append((distance + 1, neigh_row, neigh_col))

        houses = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    houses += 1
                    bfs(row, col)

        max_distance = (rows + col) * rows * cols + 1
        min_distance = max_distance
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and houses_reachable[row][col] == houses:
                    min_distance = min(min_distance, sum_distance[row][col])

        return min_distance if min_distance < max_distance else -1
