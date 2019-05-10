class Solution:
    def generateMatrix(self, n):
        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        val = 0

        row, col = 0, 0
        vec = (0, 1)

        while row != n and matrix[row][col] == -1:
            val += 1
            matrix[row][col] = val

            row, col = tuple(map(lambda x, y: x + y, (row, col), vec))

            if row == n or col == n or matrix[row][col] > 0:
                row, col = tuple(map(lambda x, y: x - y, (row, col), vec))
                vec = (vec[1], - vec[0])
                row, col = tuple(map(lambda x, y: x + y, (row, col), vec))

        return matrix
