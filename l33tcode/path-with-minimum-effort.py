import heapq
from typing import Dict, List, Tuple, Iterator


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
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    effort = abs(heights[neigh_row][neigh_col] - heights[row][col])
                    yield effort, neigh_row, neigh_col

        heap = [(0, 0, 0)]
        cell_to_effort: Dict[Tuple[int, int], int] = {}
        min_effort = -1

        while heap:
            effort, row, col = heapq.heappop(heap)
            if (row, col) == (rows - 1, cols - 1):
                min_effort = effort
                break

            for neigh_effort, neigh_row, neigh_col in neighbors(row, col):
                neigh_effort = max(effort, neigh_effort)
                if (
                    cell_to_effort.get((neigh_row, neigh_col), float("+inf"))
                    > neigh_effort
                ):
                    cell_to_effort[(neigh_row, neigh_col)] = neigh_effort
                    heapq.heappush(heap, (neigh_effort, neigh_row, neigh_col))

        return min_effort
