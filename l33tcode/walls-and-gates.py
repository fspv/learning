from typing import Set, Tuple, List, Iterator
from collections import deque
import heapq

inf = 2 ** 31 - 1
GATE, WALL = 0, -1


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0]) if rooms else 0

        def neighbours(
            row: int, col: int, visited: Set[Tuple[int, int]]
        ) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if not (0 <= neigh_row < len(rooms)) or not (
                    0 <= neigh_col < len(rooms[0])
                ):
                    continue

                if (neigh_row, neigh_col) not in visited and rooms[neigh_row][
                    neigh_col
                ] not in {WALL, GATE}:
                    yield neigh_row, neigh_col

        def dijkstra(row: int, col: int) -> None:
            visited = set()
            heap = [(0, row, col)]

            while heap:
                cur_dist, cur_row, cur_col = heapq.heappop(heap)

                rooms[cur_row][cur_col] = min(rooms[cur_row][cur_col], cur_dist)

                visited.add((cur_row, cur_col))

                for neigh_row, neigh_col in neighbours(cur_row, cur_col, visited):
                    heapq.heappush(heap, (cur_dist + 1, neigh_row, neigh_col))

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == GATE:
                    dijkstra(row, col)
