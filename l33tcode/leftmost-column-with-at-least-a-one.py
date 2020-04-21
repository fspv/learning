# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        def search_one_in_row(
            binaryMatrix: "BinaryMatrix", row: int, left: int, right: int
        ) -> int:
            while right - left > 1:
                middle = (left + right) // 2
                middle_val = binaryMatrix.get(row, middle)
                if middle_val == 0:
                    left = middle
                else:
                    right = middle

            return right

        rows, cols = binaryMatrix.dimensions()
        left, right = -1, cols

        for row in range(rows):
            one = search_one_in_row(binaryMatrix, row, left, right)
            right = min(one, right)

        return right if right < cols else -1
