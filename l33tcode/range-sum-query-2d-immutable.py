from itertools import accumulate

class NumMatrix:

    def __init__(self, matrix):
        height = len(matrix)
        width = len(matrix[0]) if height > 0 else 0

        # ss - straight sum (moving right-left, top-bottom)
        ss = [[0] * (width + 1)] + [[] for _ in range(height)]
        rs = [[0] * (width + 1)] + [[] for _ in range(height)]

        for row in range(height):
            ss[row + 1] = [0] + list(accumulate(matrix[row]))
            ss[row + 1] = list(map(lambda x, y: x + y, ss[row + 1], ss[row]))

        self.ss = ss
        self.rows = height
        self.cols = width

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows, cols, ss = self.rows, self.cols, self.ss
        return ss[row2 + 1][col2 + 1] + ss[row1][col1] - \
               ss[row1][col2 + 1] - ss[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

s = NumMatrix(matrix)
assert s.sumRegion(2, 1, 4, 3) == 8
assert s.sumRegion(1, 1, 2, 2) == 11
assert s.sumRegion(1, 2, 2, 4) == 12

s = NumMatrix([])
