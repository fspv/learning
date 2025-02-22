from collections import deque
from typing import Deque, Iterator


class Solution:
    def shortestDistance(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> int:
        rows, cols = len(maze), len(maze[0])
        visited: set[tuple[int, int, int, int]] = set()

        def hit_the_wall(row: int, col: int, row_dir: int, col_dir: int) -> bool:
            return not (
                0 <= row + row_dir < rows
                and 0 <= col + col_dir < cols
                and maze[row + row_dir][col + col_dir] == 0
            )

        def neighbours(row: int, col: int) -> Iterator[tuple[int, int, int, int]]:
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and maze[next_row][next_col] == 0
                ):
                    yield (next_row, next_col, next_row - row, next_col - col)

        queue: Deque[tuple[int, int, int, int, int]] = (
            deque()
        )  # row, col, row_direction, col_direction, distance

        for row_dir, col_dir in (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ):
            queue.append((start[0], start[1], row_dir, col_dir, 0))
            visited.add((start[0], start[1], row_dir, col_dir))

        while queue:
            row, col, row_dir, col_dir, distance = queue.popleft()

            if hit_the_wall(row, col, row_dir, col_dir) and [row, col] == destination:
                return distance

            for next_row, next_col, next_row_dir, next_col_dir in (
                neighbours(row, col)
                if hit_the_wall(row, col, row_dir, col_dir)
                else ((row + row_dir, col + col_dir, row_dir, col_dir),)
            ):
                if (next_row, next_col, next_row_dir, next_col_dir) in visited:
                    continue
                visited.add((next_row, next_col, next_row_dir, next_col_dir))
                queue.append(
                    (next_row, next_col, next_row_dir, next_col_dir, distance + 1)
                )

        return -1
