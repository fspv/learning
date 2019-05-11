import bisect

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        right = len(matrix[0])

        for row in range(len(matrix)):
            right = bisect.bisect_left(matrix[row], target, 0, right)

            if right < len(matrix[0]) and matrix[row][right] == target:
                return True

        return False
