import heapq
from typing import Iterator, List, Tuple


class Solution:
    def findShortestWay(
        self, maze: List[List[int]], ball: List[int], hole: List[int]
    ) -> str:
        rows, cols = len(maze), len(maze[0]) if maze else 0

        def calculate_possible_jumps() -> List[List[List[Tuple[int, int]]]]:
            # L, U, R, D
            result = [
                [
                    [(-1, -1)] * 4 if maze[row][col] == 1 else [(row, col)] * 4
                    for col in range(cols)
                ]
                for row in range(rows)
            ]

            # LR, TD
            for row in range(rows):
                for col in range(cols):
                    if maze[row][col] == 1:
                        # Wall
                        continue

                    for pos, neigh_row, neigh_col in (
                        (0, row, col - 1),  # Left
                        (1, row - 1, col),  # Up
                    ):
                        if (
                            0 <= neigh_row < rows
                            and 0 <= neigh_col < cols
                            and (row, col) != (hole[0], hole[1])
                            and result[neigh_row][neigh_col][0] != (-1, -1)
                        ):
                            result[row][col][pos] = result[neigh_row][neigh_col][pos]

            # RL, BU
            for row in reversed(range(rows)):
                for col in reversed(range(cols)):
                    if maze[row][col] == 1:
                        # Wall
                        continue

                    for pos, neigh_row, neigh_col in (
                        (2, row, col + 1),  # Right
                        (3, row + 1, col),  # Down
                    ):
                        if (
                            0 <= neigh_row < rows
                            and 0 <= neigh_col < cols
                            and (row, col) != (hole[0], hole[1])
                            and result[neigh_row][neigh_col][0] != (-1, -1)
                        ):
                            result[row][col][pos] = result[neigh_row][neigh_col][pos]

            return result

        # Calculate possible jumps from cell
        possible_jumps: List[List[List[Tuple[int, int]]]] = calculate_possible_jumps()

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in possible_jumps[row][col]:
                if (neigh_row, neigh_col) != (row, col):
                    yield neigh_row, neigh_col

        # Run Dijkstra on the set
        heap: List[Tuple[int, str, int, int]] = []  # (distance, direction, row, column)

        heapq.heappush(heap, (0, "", ball[0], ball[1]))
        parent: List[List[Tuple[int, int]]] = [
            [(row, col) for col in range(cols)] for row in range(rows)
        ]
        distances: List[List[Tuple[int, str]]] = [
            [(rows * cols, "") for col in range(cols)] for row in range(rows)
        ]
        distances[ball[0]][ball[1]] = (0, "")

        while heap:
            distance, direction, row, col = heapq.heappop(heap)

            if (row, col) == (hole[0], hole[1]):
                return direction

            for next_row, next_col in neighbors(row, col):
                next_distance = distance + abs(next_row - row) + abs(next_col - col)

                sign = lambda num: 0 if num == 0 else num / abs(num)

                next_direction = (
                    direction
                    + {(0, 1): "r", (0, -1): "l", (1, 0): "d", (-1, 0): "u"}[
                        sign(next_row - row), sign(next_col - col)
                    ]
                )

                if (next_distance, next_direction) >= distances[next_row][next_col]:
                    continue

                parent[next_row][next_col] = (row, col)
                distances[next_row][next_col] = (next_distance, next_direction)

                # estimation = (
                #     distances[next_row][next_col]
                #     + abs(next_row - hole[0])
                #     + abs(next_col - hole[1])
                # )

                heapq.heappush(
                    heap, (next_distance, next_direction, next_row, next_col)
                )

        return "impossible"
