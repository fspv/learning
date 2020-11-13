from typing import List, Tuple, Set, Iterator, NamedTuple


class Land(NamedTuple):
    row: int
    col: int


class Island:
    def __init__(self) -> None:
        self.land: List[Land] = []

    def add_land(self, land: Land) -> None:
        self.land.append(land)

    def rotate90(self) -> None:
        for pos in range(len(self.land)):
            land = self.land[pos]
            self.land[pos] = Land(land.col, -land.row)

    def flip_vertical(self) -> None:
        for pos in range(len(self.land)):
            land = self.land[pos]
            self.land[pos] = Land(-land.row, land.col)

    def flip_horizontal(self) -> None:
        for pos in range(len(self.land)):
            land = self.land[pos]
            self.land[pos] = Land(land.row, -land.col)

    def to_start(self) -> None:
        self.land.sort()

        start_row, start_col = self.land[0]

        for pos in range(len(self.land)):
            land = self.land[pos]
            self.land[pos] = Land(land.row - start_row, land.col - start_col)

    def normalize(self) -> None:
        islands = []

        for _ in range(4):
            self.to_start()
            islands.append(self.land.copy())

            self.flip_vertical()
            self.to_start()
            islands.append(self.land.copy())
            self.flip_vertical()

            self.flip_horizontal()
            self.to_start()
            islands.append(self.land.copy())
            self.flip_horizontal()

            self.rotate90()

        islands.sort()

        self.land = islands[0]


class Grid:
    def __init__(self, grid: List[List[int]]) -> None:
        self._grid = grid
        self._rows = len(grid)
        self._cols = len(grid[0]) if grid else 0
        self._visited: Set[Tuple[int, int]] = set()

    def _neighbors(self, row: int, col: int) -> Iterator[Tuple[int, int]]:
        for neigh_row, neigh_col in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if (
                0 <= neigh_row < self._rows
                and 0 <= neigh_col < self._cols
                and self._grid[neigh_row][neigh_col] == 1
                and (neigh_row, neigh_col) not in self._visited
            ):
                yield (neigh_row, neigh_col)

    def _traverse_island(self, row: int, col: int, island: Island) -> None:
        self._visited.add((row, col))
        for neigh_row, neigh_col in self._neighbors(row, col):
            self._traverse_island(neigh_row, neigh_col, island)

        island.add_land(Land(row, col))

    def count_islands(self) -> int:
        islands: Set[Tuple[Land, ...]] = set()

        for row in range(self._rows):
            for col in range(self._cols):
                if (row, col) not in self._visited and self._grid[row][col] == 1:
                    island = Island()
                    self._traverse_island(row, col, island)
                    island.normalize()
                    islands.add(tuple(island.land))

        return len(islands)


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        return Grid(grid).count_islands()
