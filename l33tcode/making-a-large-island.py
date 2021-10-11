from typing import Iterator, List, Set, Tuple


class UnionFind:
    def __init__(self, rows: int, cols: int) -> None:
        self._count: List[List[int]] = [[1] * cols for _ in range(rows)]
        self._parent: List[List[Tuple[int, int]]] = [
            [(row, col) for col in range(cols)] for row in range(rows)
        ]

    def find(self, row: int, col: int) -> Tuple[int, int]:
        init_row, init_col = row, col

        row, col = self._parent[row][col]

        while self._parent[row][col] != (row, col):
            row, col = self._parent[row][col]

        root_row, root_col = row, col
        row, col = init_row, init_col

        while (row, col) != (root_row, root_col):
            tmp_row, tmp_col = self._parent[row][col]
            self._parent[row][col] = root_row, root_col
            row, col = tmp_row, tmp_col

        return root_row, root_col

    def union(
        self, row_left: int, col_left: int, row_right: int, col_right: int
    ) -> None:
        if self._count[row_left][col_left] > self._count[row_right][col_right]:
            row_less, col_less, row_more, col_more = (
                row_right,
                col_right,
                row_left,
                col_left,
            )
        else:
            row_less, col_less, row_more, col_more = (
                row_left,
                col_left,
                row_right,
                col_right,
            )

        self._count[row_more][col_more] += self._count[row_less][col_less]
        self._parent[row_less][col_less] = row_more, col_more

    def count(self, row: int, col: int) -> int:
        return self._count[row][col]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        union_find = UnionFind(rows, cols)

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    if grid[neigh_row][neigh_col] == 1:
                        yield neigh_row, neigh_col

        largest_island = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                for neigh_row, neigh_col in neighbors(row, col):
                    row_left, col_left = union_find.find(row, col)
                    row_right, col_right = union_find.find(neigh_row, neigh_col)

                    if (row_left, col_left) != (row_right, col_right):
                        union_find.union(row_left, col_left, row_right, col_right)

                root_row, root_col = union_find.find(row, col)
                largest_island = max(
                    largest_island, union_find.count(root_row, root_col)
                )

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    count = 1

                    known_roots: Set[Tuple[int, int]] = set()

                    for neigh_row, neigh_col in neighbors(row, col):
                        root_row, root_col = union_find.find(neigh_row, neigh_col)
                        if (root_row, root_col) not in known_roots:
                            count += union_find.count(root_row, root_col)
                            known_roots.add((root_row, root_col))

                    largest_island = max(largest_island, count)

        return largest_island
