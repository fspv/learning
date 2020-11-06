import heapq
from typing import List, Tuple, Iterator
from collections import defaultdict
from functools import lru_cache


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0]) if heights else 0

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                ):
                    yield (
                        abs(heights[neigh_row][neigh_col] - heights[row][col]),
                        neigh_row,
                        neigh_col,
                    )

        heap = [(0, 0, 0)]
        efforts = defaultdict(lambda: float("+inf"))

        while heap:
            effort, row, col = heapq.heappop(heap)

            if (row, col) == (rows - 1, cols - 1):
                return effort

            for neigh_effort, neigh_row, neigh_col in neighbors(row, col):
                cur_effort = max(effort, neigh_effort)
                if efforts[(neigh_row, neigh_col)] > cur_effort:
                    efforts[(neigh_row, neigh_col)] = cur_effort
                    heapq.heappush(heap, (cur_effort, neigh_row, neigh_col))

    def minimumEffortPathBacktrack(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0]) if heights else 0

        visited = set()

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int, int]]:
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
                ):
                    yield (
                        abs(heights[neigh_row][neigh_col] - heights[row][col]),
                        neigh_row,
                        neigh_col,
                    )

        def backtrack(row: int, col: int) -> int:
            if (row, col) == (rows - 1, cols - 1):
                return 0

            min_effort = float("+inf")

            visited.add((row, col))

            for neigh_effort, neigh_row, neigh_col in neighbors(row, col):
                min_effort = min(
                    min_effort, max(backtrack(neigh_row, neigh_col), neigh_effort)
                )

            visited.remove((row, col))

            return min_effort

        return backtrack(0, 0)
