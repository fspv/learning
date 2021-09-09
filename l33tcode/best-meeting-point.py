from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        def median(numbers: List[int]) -> int:
            tmp = list(sorted(numbers))

            return tmp[len(tmp) // 2]

        x: List[int] = []
        y: List[int] = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    x.append(row)
                    y.append(col)

        x_med = median(x)
        y_med = median(y)

        distance = 0
        for x, y in zip(x, y):
            distance += abs(x - x_med) + abs(y - y_med)

        return distance
