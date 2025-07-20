import unittest
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(array: List[int], pos: int) -> int:
            root = pos
            while root != array[root]:
                root = array[root]

            while pos != root:
                array[pos], pos = root, array[pos]

            return root

        def union(root_left: int, root_right: int, array: List[int], count: List[int]):
            root_less, root_more = sorted(
                (root_left, root_right), key=lambda x: count[x]
            )
            array[root_less] = root_more
            count[root_more] += count[root_less]

        rows, cols = len(grid), len(grid[0]) if grid else 0
        array = list(range(rows * cols))
        count = [1] * (rows * cols)
        islands = rows * cols

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    islands -= 1
                    continue
                for row_next, col_next in [
                    (row, col - 1),
                    (row - 1, col),
                ]:
                    if (
                        0 <= row_next < rows
                        and 0 <= col_next < cols
                        and grid[row_next][col_next] == "1"
                    ):
                        root_left = find(array, row * cols + col)
                        root_right = find(array, row_next * cols + col_next)
                        if root_left != root_right:
                            union(root_left, root_right, array, count)
                            islands -= 1

        return islands

    def numIslandsDFSIter(self, grid: "List[List[str]]") -> "int":
        visited = set()
        islands_count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x, y) not in visited and int(grid[y][x]):
                    islands_count += 1

                    stack = [(x, y)]

                    while len(stack):
                        point = stack.pop()
                        visited.add(point)

                        neighbours = [
                            (point[0] - 1, point[1]),
                            (point[0] + 1, point[1]),
                            (point[0], point[1] + 1),
                            (point[0], point[1] - 1),
                        ]

                        for neigh in neighbours:
                            if (
                                neigh[0] >= len(grid[0])
                                or neigh[0] < 0
                                or neigh[1] >= len(grid)
                                or neigh[1] < 0
                            ):
                                continue

                            if not int(grid[neigh[1]][neigh[0]]):
                                continue

                            if neigh not in visited:
                                stack.append(neigh)

        return islands_count

    def numIslandsBFS(self, grid):
        queue = deque()
        visited = {}
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and int(grid[i][j]) == 1:
                    islands += 1
                    queue.append((i, j))

                    while len(queue):
                        m, n = queue.popleft()

                        if m < 0 or m >= len(grid) or n < 0 or n >= len(grid[0]):
                            continue

                        if (m, n) in visited:
                            continue

                        visited[(m, n)] = True

                        if int(grid[m][n]) == 0:
                            continue

                        neighbours = [
                            (m - 1, n),
                            (m + 1, n),
                            (m, n - 1),
                            (m, n + 1),
                        ]

                        for neighbour in neighbours:
                            queue.append(neighbour)

        return islands


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.numIslands([]), 0)

    def test_just_zero(self):
        self.assertEqual(self.sol.numIslands([["0"]]), 0)

    def test_just_one(self):
        self.assertEqual(self.sol.numIslands([["1"]]), 1)

    def test_1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test_2(self):
        grid = [
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.sol.numIslands(grid), 2)

    def test_3(self):
        grid = [
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "1"],
        ]
        self.assertEqual(self.sol.numIslands(grid), 4)

    def test_4(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(self.sol.numIslands(grid), 3)
