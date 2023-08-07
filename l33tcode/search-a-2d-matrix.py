from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def get_value(pos: int):
            row, col = pos // len(matrix[0]), pos % len(matrix[0])
            return matrix[row][col]

        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left < right:
            mid = left + (right - left) // 2

            if get_value(mid) < target:
                left = mid + 1
            elif get_value(mid) >= target:
                right = mid

        return get_value(left) == target
