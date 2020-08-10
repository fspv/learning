from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        def create_matrix(rows: int, cols: int) -> List[List[int]]:
            return [[0] * cols for _ in range(rows)]

        rows, cols = len(mat), len(mat[0]) if mat else 0
        dp = create_matrix(rows, cols)

        for row in range(rows):
            for col in range(cols):
                upper, upper_left, left = 0, 0, 0

                if row > 0:
                    upper = dp[row - 1][col]
                if col > 0:
                    left = dp[row][col - 1]
                if row > 0 and col > 0:
                    upper_left = dp[row - 1][col - 1]

                dp[row][col] = upper - upper_left + left + mat[row][col]

        result = create_matrix(rows, cols)

        for row in range(rows):
            for col in range(cols):
                right_bottom, right_top = 0, 0
                left_bottom, left_top = 0, 0

                right_bottom = dp[min(row + K, rows - 1)][min(col + K, cols - 1)]
                if row - K > 0:
                    right_top = dp[row - K - 1][min(col + K, cols - 1)]

                if col - K > 0:
                    left_bottom = dp[min(row + K, rows - 1)][col - K - 1]

                if row - K > 0 and col - K > 0:
                    left_top = dp[row - K - 1][col - K - 1]

                result[row][col] = right_bottom - right_top - left_bottom + left_top

        return result
