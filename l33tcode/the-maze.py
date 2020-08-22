from contextlib import contextmanager
from typing import Iterator, Tuple, List, Set
from collections import deque

WALL, EMPTY = 1, 0


@contextmanager
def visited_manager(
    visited: Set[Tuple[int, int, Tuple[int, int]]],
    row: int,
    col: int,
    direction: Tuple[int, int],
) -> Iterator:
    visited.add((row, col, direction))
    yield


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        visited: Set[Tuple[int, int]] = set()

        def is_wall(row: int, col: int, direction: Tuple[int, int]) -> bool:
            rows, cols = len(maze), len(maze[0]) if maze else 0
            next_row, next_col = row + direction[0], col + direction[1]

            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and maze[next_row][next_col] != WALL
            ):
                return False

            return True

        def directions(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for direction in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ):
                yield direction

        def follow_direction(
            row: int, col: int, direction: Tuple[int, int]
        ) -> Tuple[int, int]:
            while not is_wall(row, col, direction):
                row, col = row + direction[0], col + direction[1]

            return row, col

        queue: deque = deque()

        queue.append(tuple(start))

        while queue:
            row, col = queue.popleft()

            if [row, col] == destination:
                return True

            for direction in directions(row, col):
                next_row, next_col = follow_direction(row, col, direction)
                if (next_row, next_col) not in visited:
                    queue.append((next_row, next_col))
                    visited.add((next_row, next_col))

        return False

    def hasPathDFS(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        visited: Set[Tuple[int, int, Tuple[int, int]]] = set()

        def is_wall(row: int, col: int, direction: Tuple[int, int]) -> bool:
            rows, cols = len(maze), len(maze[0]) if maze else 0
            next_row, next_col = row + direction[0], col + direction[1]

            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and maze[next_row][next_col] != WALL
            ):
                return False

            return True

        def directions(row: int, col: int) -> Iterator[Tuple[int, int]]:
            rows, cols = len(maze), len(maze[0]) if maze else 0

            for direction in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ):
                next_row, next_col = row + direction[0], col + direction[1]

                if (
                    not is_wall(row, col, direction)
                    and (next_row, next_col, direction) not in visited
                ):
                    yield direction

        def backtrack(row: int, col: int, direction: Tuple[int, int]) -> bool:
            if [row, col] == destination and is_wall(row, col, direction):
                return True

            next_directions = iter([direction])

            if is_wall(row, col, direction):
                next_directions = directions(row, col)

            for next_direction in next_directions:
                with visited_manager(visited, row, col, direction):
                    if backtrack(
                        row + next_direction[0],
                        col + next_direction[1],
                        next_direction,
                    ):
                        return True

            return False

        for direction in directions(start[0], start[1]):
            if backtrack(start[0], start[1], direction):
                return True

        return False
