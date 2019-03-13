import unittest


class Solution:
    def reverseString(self, s):
        if not s:
            return

        for pos in range(int(len(s) / 2)):
            s[pos], s[len(s) - pos - 1] = s[len(s) - pos - 1], s[pos]

    def reverseStringRecursive(self, s, left=None, right=None):
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or (left is not None and right is not None and left >= right):
            return

        if left is None and right is None:
            left = 0
            right = len(s) - 1

        s[left], s[right] = s[right], s[left]

        self.reverseString(s, left + 1, right - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty1(self):
        self.assertIsNone(self.sol.reverseString(None))

    def test_empty2(self):
        self.assertIsNone(self.sol.reverseString([]))

    def test_one(self):
        s = [1]
        self.sol.reverseString(s)
        self.assertListEqual(s, [1])

    def test_two(self):
        s = [1, 2]
        self.sol.reverseString(s)
        self.assertListEqual(s, [2, 1])

    def test_three(self):
        s = [1, 2, 3]
        self.sol.reverseString(s)
        self.assertListEqual(s, [3, 2, 1])

    def test_ten(self):
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.sol.reverseString(s)
        self.assertListEqual(s, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_eleven(self):
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.sol.reverseString(s)
        self.assertListEqual(s, [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
