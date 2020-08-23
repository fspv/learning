class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        diags = rows + cols

        for diag in range(rows):
            value = matrix[diag][0]
            for pos in range(min(rows, cols) - max(0, (diag - max(0, (rows - cols))))):
                row, col = pos + diag, pos
                if value != matrix[row][col]:
                    return False

        for diag in range(cols):
            value = matrix[0][diag]
            for pos in range(min(rows, cols) - max(0, (diag - max(0, (cols - rows))))):
                row, col = pos, pos + diag
                if value != matrix[row][col]:
                    return False

        return True
