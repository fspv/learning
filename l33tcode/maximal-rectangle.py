from typing import List, Tuple, Iterator
from functools import lru_cache


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        def calc_heights(matrix: List[List[str]]) -> Iterator[List[int]]:
            heights = [0] * cols
            for row in range(rows):
                new_heights = [0] * cols
                for col in range(cols):
                    if matrix[row][col] == "1":
                        new_heights[col] = heights[col] + 1

                heights = new_heights
                yield heights

        def max_histogram_rectangle(heights: List[int]) -> int:
            area = 0

            stack: List[int] = []

            for pos, height in enumerate(heights):
                while stack and heights[stack[-1]] >= height:
                    last_pos = stack.pop()

                    first_less = stack[-1] if stack else -1

                    area = max(area, (pos - (first_less + 1)) * heights[last_pos])

                stack.append(pos)

            while stack:
                pos = stack.pop()
                first_less = stack[-1] if stack else -1
                area = max(area, (len(heights) - (first_less + 1)) * heights[pos])

            return area

        area = 0
        for heights in calc_heights(matrix):
            area = max(area, max_histogram_rectangle(heights))

        return area

    def maximalRectangleN4(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        def index_matrix(
            matrix: List[List[str]],
        ) -> Tuple[List[List[int]], List[List[int]]]:
            ones_left = [[0] * cols for _ in range(rows)]
            ones_above = [[0] * cols for _ in range(rows)]

            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col] == "1":
                        ones_left[row][col] = 1
                        if col > 0:
                            ones_left[row][col] += ones_left[row][col - 1]

            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col] == "1":
                        ones_above[row][col] = 1
                        if row > 0:
                            ones_above[row][col] += ones_above[row - 1][col]

            return ones_left, ones_above

        ones_left, ones_above = index_matrix(matrix)

        @lru_cache(None)
        def dfs(row: int, col: int, height: int, width: int) -> int:
            area = height * width

            if row + 1 < rows and ones_left[row + 1][col] >= width:
                area = max(area, dfs(row + 1, col, height + 1, width))

            if col + 1 < cols and ones_above[row][col + 1] >= height:
                area = max(area, dfs(row, col + 1, height, width + 1))

            return area

        area = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    area = max(area, dfs(row, col, 1, 1))

        return area
