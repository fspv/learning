from typing import List, Iterator, Tuple
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        distances = [[float("+inf")] * len(grid[r]) for r in range(len(grid))]
        rows, cols = len(grid), len(grid[0]) if grid else 0

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            # Return all neighbors up, down, left, right if exist
            for neigh_row, neigh_col in (
                (row, col - 1),
                (row - 1, col),
                (row, col + 1),
                (row + 1, col),
            ):
                if (
                    neigh_row >= 0
                    and neigh_row < rows
                    and neigh_col >= 0
                    and neigh_col < cols
                    and grid[neigh_row][neigh_col] == 1
                ):
                    yield neigh_row, neigh_col

        def dfs(row, col, distance) -> None:
            if distance > distances[row][col]:
                return

            distances[row][col] = distance

            for neigh_row, neigh_col in neighbors(row, col):
                dfs(neigh_row, neigh_col, distance + 1)

        def get_last_rotten() -> int:
            result = 0

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1:
                        if distances[row][col] == float("+inf"):
                            return -1
                        else:
                            result = max(result, int(distances[row][col]))

            return result

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    dfs(row, col, 0)

        return get_last_rotten()

    def orangesRottingBFS(self, grid: List[List[int]]) -> int:
        distances = [[float("+inf")] * len(grid[r]) for r in range(len(grid))]
        rows, cols = len(grid), len(grid[0]) if grid else 0

        def neighbors(row, col):
            # Return all neighbors up, down, left, right if exist
            for neigh_row, neigh_col in (
                (row, col - 1),
                (row - 1, col),
                (row, col + 1),
                (row + 1, col),
            ):
                if (
                    neigh_row >= 0
                    and neigh_row < rows
                    and neigh_col >= 0
                    and neigh_col < cols
                    and grid[neigh_row][neigh_col] == 1
                ):
                    yield neigh_row, neigh_col

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    distances[row][col] = 0

        while queue:
            row, col, distance = queue.popleft()

            if distance > distances[row][col]:
                continue

            distances[row][col] = distance

            for neigh_row, neigh_col in neighbors(row, col):
                queue.append((neigh_row, neigh_col, distance + 1))

        result = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if distances[row][col] == float("+inf"):
                        return -1

                    result = max(result, distances[row][col])

        return result

    def orangesRottingBFS2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        queue = deque()
        visited = set()
        fresh = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    visited.add((row, col))
                    fresh.add((row, col))
                if grid[row][col] == 1:
                    fresh.add((row, col))

        def neighbours(
            row: int, col: int, rows: int, cols: int
        ) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    if (neigh_row, neigh_col) not in visited and grid[neigh_row][
                        neigh_col
                    ] == 1:
                        yield (neigh_row, neigh_col)

        total = 0

        while queue:
            row, col, minutes = queue.popleft()
            fresh.remove((row, col))
            total = max(total, minutes)

            for neigh_row, neigh_col in neighbours(row, col, rows, cols):
                queue.append((neigh_row, neigh_col, minutes + 1))
                visited.add((neigh_row, neigh_col))

        return -1 if fresh else total
