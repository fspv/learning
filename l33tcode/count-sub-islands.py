from typing import Iterator, List, Tuple


class UnionFind:
    def __init__(self, size: int) -> None:
        self._roots = list(range(size))
        self._counts = [1] * size

    def union(self, root_left: int, root_right: int) -> None:
        root_less, root_more = tuple(
            sorted([root_left, root_right], key=lambda x: self._counts[x])
        )

        self._counts[root_more] += self._counts[root_less]
        self._roots[root_less] = root_more

    def find(self, vertex: int) -> int:
        if self._roots[vertex] == vertex:
            return vertex

        root = self.find(self._roots[vertex])
        self._roots[vertex] = root

        return root


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0]) if grid1 else 0

        if len(grid2) != rows or (len(grid2[0]) if grid2 else 0) != cols:
            raise ValueError("Both grids should be of the same size")

        def neighbors(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1),
            ):
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    yield neigh_row, neigh_col

        union_find = UnionFind(rows * cols)

        for row in range(rows):
            for col in range(cols):
                if grid1[row][col] == 0 or grid2[row][col] == 0:
                    continue
                for neigh_row, neigh_col in neighbors(row, col):
                    if (
                        grid1[neigh_row][neigh_col] == 1
                        and grid2[neigh_row][neigh_col] == 1
                    ):
                        root = union_find.find(row * cols + col)
                        neigh_root = union_find.find(neigh_row * cols + neigh_col)

                        if root != neigh_root:
                            union_find.union(root, neigh_root)

        visited: List[List[bool]] = [[False] * cols for _ in range(rows)]

        def dfs(row: int, col: int) -> bool:
            visited[row][col] = True
            root = union_find.find(row * cols + col)

            fits = True

            for neigh_row, neigh_col in neighbors(row, col):
                if grid2[neigh_row][neigh_col] == 0:
                    continue

                neigh_root = union_find.find(neigh_row * cols + neigh_col)

                if root != neigh_root:
                    fits = False
                    continue

                if visited[neigh_row][neigh_col]:
                    continue

                fits = dfs(neigh_row, neigh_col) and fits

            return fits

        islands = 0

        for row in range(rows):
            for col in range(cols):
                if (
                    not visited[row][col]
                    and grid1[row][col] == 1
                    and grid2[row][col] == 1
                ):
                    islands += dfs(row, col)

        return islands
