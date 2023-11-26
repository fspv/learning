from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        cache: List[List[int]] = [matrix[row].copy() for row in range(rows)]

        for col in range(cols):
            for row in range(1, rows):
                if matrix[row][col] == 1:
                    cache[row][col] = cache[row - 1][col] + 1

        max_area = 0

        for row in range(rows):
            cache[row].sort(reverse=True)

            for col in range(cols):
                max_area = max(max_area, (col + 1) * cache[row][col])

        return max_area
