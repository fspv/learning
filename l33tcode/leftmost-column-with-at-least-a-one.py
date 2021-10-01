# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binary_matrix: "BinaryMatrix") -> int:
        rows, cols = binary_matrix.dimensions()

        def has_one(col: int) -> bool:
            for row in range(rows):
                if binary_matrix.get(row, col) == 1:
                    return True

            return False

        left, right = 0, cols

        while left < right:
            middle = (right - left) // 2 + left

            if has_one(middle):
                right = middle
            else:
                left = middle + 1

        return left if 0 <= left < cols else -1

    def leftMostColumnWithOne2(self, binaryMatrix: "BinaryMatrix") -> int:
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
