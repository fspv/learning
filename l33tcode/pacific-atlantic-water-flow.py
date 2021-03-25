from collections import deque
from typing import List, Deque, Tuple, Set, Iterator


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    if matrix[row][col] <= matrix[neigh_row][neigh_col]:
                        yield (neigh_row, neigh_col)

        def bfs(init_row: int, init_col: int) -> List[List[bool]]:
            """
            init_row, init_col - row and col we use to init bfs
            returns: matrix with all the reachable positions
            """
            queue: Deque[Tuple[int, int]] = deque()
            seen: Set[Tuple[int, int]] = set()

            for row in range(rows):
                queue.append((row, init_col))
            for col in range(cols):
                queue.append((init_row, col))

            reachable: List[List[bool]] = [[False] * cols for row in range(rows)]

            while queue:
                row, col = queue.popleft()

                reachable[row][col] = True

                for neigh_row, neigh_col in neighbors(row, col):
                    if (neigh_row, neigh_col) not in seen:
                        queue.append((neigh_row, neigh_col))
                        seen.add((neigh_row, neigh_col))

            return reachable

        reachable_pacific = bfs(0, 0)
        reachable_atlantic = bfs(rows - 1, cols - 1)

        result: List[List[int]] = []

        for row in range(rows):
            for col in range(cols):
                if reachable_pacific[row][col] and reachable_atlantic[row][col]:
                    result.append([row, col])

        return result
