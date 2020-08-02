from typing import Set, Tuple, List, Iterator
from collections import deque
import heapq

inf = 2 ** 31 - 1
GATE, WALL = 0, -1


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def neighbours(
            row: int, col: int, visited: Set[Tuple[int, int]]
        ) -> Iterator[Tuple[int, int]]:
            """
            Get all neighbours for this room which are not out of boundaries,
            not visited yet and not either wall or gate
            """
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

        visited = set()
        heap: List[Tuple[int, int, int]] = []

        rows, cols = len(rooms), len(rooms[0]) if rooms else 0
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == GATE:
                    heapq.heappush(heap, (0, row, col))

        while heap:
            dist, row, col = heapq.heappop(heap)

            visited.add((row, col))

            for neigh_row, neigh_col in neighbours(row, col, visited):
                if dist + 1 < rooms[neigh_row][neigh_col]:
                    rooms[neigh_row][neigh_col] = dist + 1
                    heapq.heappush(heap, (dist + 1, neigh_row, neigh_col))
