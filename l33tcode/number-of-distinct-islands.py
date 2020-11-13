from enum import Enum
from typing import List, Tuple, Set, Iterator


class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


direction_opposite = {
    Direction.NONE: Direction.NONE,
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
}


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        seen: Set[Tuple[int, int]] = set()

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int, Direction]]:
            for neigh_row, neigh_col, neigh_direction in (
                (row - 1, col, Direction.DOWN),
                (row + 1, col, Direction.UP),
                (row, col - 1, Direction.LEFT),
                (row, col + 1, Direction.RIGHT),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and grid[neigh_row][neigh_col] == 1
                ):
                    yield (neigh_row, neigh_col, neigh_direction)

        def dfs(
            row: int, col: int, path: List[Direction], direction: Direction
        ) -> None:
            seen.add((row, col))
            for neigh_row, neigh_col, neigh_direction in neighbors(row, col):
                if (neigh_row, neigh_col) not in seen:
                    path.append(neigh_direction)
                    dfs(neigh_row, neigh_col, path, neigh_direction)
                    path.append(direction_opposite[neigh_direction])

        paths: Set[Tuple[Direction, ...]] = set()
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    path: List[Direction] = []
                    dfs(row, col, path, Direction.NONE)
                    paths.add(tuple(path))

        return len(paths)

    def numDistinctIslandsCoordinates(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        seen: Set[Tuple[int, int]] = set()

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and grid[neigh_row][neigh_col] == 1
                ):
                    yield (neigh_row, neigh_col)

        def dfs(
            init_row: int,
            init_col: int,
            row: int,
            col: int,
            island: List[Tuple[int, int]],
        ) -> None:
            seen.add((row, col))
            for neigh_row, neigh_col in neighbors(row, col):
                if (neigh_row, neigh_col) not in seen:
                    dfs(init_row, init_col, neigh_row, neigh_col, island)

            island.append((row - init_row, col - init_col))

        islands: Set[Tuple[Tuple[int, int], ...]] = set()
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    island: List[Tuple[int, int]] = []
                    dfs(row, col, row, col, island)
                    islands.add(tuple(island))

        return len(islands)
