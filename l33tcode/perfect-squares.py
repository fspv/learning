import unittest
from collections import deque

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        perfect_squares = []

        for num in range(1, n + 1):
            if self.is_perfect_square(num):
                perfect_squares.append(num)


        queue = deque()
        queue.append((0, 0))
        level_width = 1
        level = 0

        while len(queue):
            if level_width == 0:
                level_width = len(queue)
                level += 1

            prev_val, prev_sum = queue.popleft()

            for sq in perfect_squares:
                if sq + prev_sum > n:
                    break

                if sq + prev_sum == n:
                    return level + 1

                queue.append((sq, sq + prev_sum))

            level_width -= 1

    def is_perfect_square(self, num, left=0, right=None):
        if num < 2:
            return True

        if right is None:
            right = num

        mid = int((right + left) / 2)

        if mid ** 2 == num:
            return True
        elif mid == left or mid < 2:
            return False
        else:
            if mid ** 2 > num:
                right = mid
            else:
                left = mid
            return self.is_perfect_square(num, left=left, right=right)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sol(self):
        self.assertEqual(self.sol.numSquares(0), 0)
        self.assertEqual(self.sol.numSquares(1), 1)
        self.assertEqual(self.sol.numSquares(12), 3)
        self.assertEqual(self.sol.numSquares(13), 2)
        self.assertEqual(self.sol.numSquares(141), 3)
        self.assertEqual(self.sol.numSquares(7168), 4)

unittest.main()
