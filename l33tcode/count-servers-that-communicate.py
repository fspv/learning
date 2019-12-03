from typing import List
from collections import defaultdict


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(set), defaultdict(set)
        connected = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    if row in rows or col in cols:
                        if len(rows[row]) == 1:
                            connected.add(list(rows[row])[0])
                        if len(cols[col]) == 1:
                            connected.add(list(cols[col])[0])
                        connected.add((row, col))
                    rows[row].add((row, col))
                    cols[col].add((row, col))

        return len(connected)


    def countServersNoMem(self, grid: List[List[int]]) -> int:
        # left-right
        for row in range(len(grid)):
            first = None
            for col in range(len(grid[0])):
                if grid[row][col]:
                    if first is not None:
                        grid[row][col] += 1
                        grid[row][first] += 1
                    else:
                        first = col

        # top-down
        for col in range(len(grid[0])):
            first = None
            for row in range(len(grid)):
                if grid[row][col]:
                    if first is not None:
                        grid[row][col] += 1
                        grid[first][col] += 1
                    else:
                        first = row

        # Count result
        count = 0
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                count += 1 if grid[row][col] > 1 else 0

        return count


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.countServers([[0]]) == 0
        assert self.sol.countServers([[1]]) == 0

    def test_case1(self):
        assert self.sol.countServers([[1,0],[0,1]]) == 0

    def test_case2(self):
        assert self.sol.countServers([[1,0],[1,1]]) == 3

    def test_case3(self):
        assert self.sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4

    def test_case4(self):
        assert self.sol.countServers([[1,1,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,1]]) == 5

    def test_case5(self):
        assert self.sol.countServers(
            [
                [0,0,1,0,1],
                [0,1,0,1,0],
                [0,1,1,1,0],
                [1,0,0,1,1],
                [0,0,1,1,0]
            ]
        ) == 12
