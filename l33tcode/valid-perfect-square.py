import unittest

# TODO: In this file I used the dumbest method after bruteforce. Have to
# learn to implement another methods

class Solution:
    def find_sqrt(self, num, left=0, right=None):
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
            return self.find_sqrt(num, left=left, right=right)

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True

        return self.find_sqrt(num, left=0, right=num)

class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sol(self):
        self.assertTrue(self.sol.isPerfectSquare(0))
        self.assertTrue(self.sol.isPerfectSquare(1))
        self.assertFalse(self.sol.isPerfectSquare(2))
        self.assertFalse(self.sol.isPerfectSquare(3))
        self.assertTrue(self.sol.isPerfectSquare(4))
        self.assertFalse(self.sol.isPerfectSquare(5))
        self.assertFalse(self.sol.isPerfectSquare(14))
        self.assertTrue(self.sol.isPerfectSquare(16))
        self.assertFalse(self.sol.isPerfectSquare(17))
        self.assertFalse(self.sol.isPerfectSquare(19))
        self.assertFalse(self.sol.isPerfectSquare(21))
        self.assertTrue(self.sol.isPerfectSquare(25))

unittest.main()

