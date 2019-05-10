class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = col0 = 1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 and matrix[row][col] == 0:
                    row0 = 0
                elif col == 0 and matrix[row][col] == 0:
                    col0 = 0
                else:
                    if matrix[row][col] == 0:
                        matrix[0][col] = 0
                        matrix[row][0] = 0

        for row in reversed(range(len(matrix))):
            for col in reversed(range(len(matrix[0]))):
                if row == 0 and row0 == 0:
                    matrix[row][col] = 0
                elif col == 0 and col0 == 0:
                    matrix[row][col] = 0
                elif matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
