import unittest

# Loop invariant:
#   On k-th step
#       * D contains number of columns from 0 to k that are not sorted in a
#         non-decreasing order
# Measure of progress: each step we move one column to the right
# Main Steps: Go through every column and add it to D if it is not sorted
#   ascending

class Solution:
    def minDeletionSize(self, A: 'List[str]') -> 'int':
        D = 0

        for column in range(len(A[0])):
            for row in range(1, len(A)):
                if A[row][column] < A[row - 1][column]:
                    D += 1
                    break

        return D


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one(self):
        self.assertEqual(self.sol.minDeletionSize(["a"]), 0)
        self.assertEqual(self.sol.minDeletionSize(["a", "b"]), 0)

    def test_multiple1(self):
        self.assertEqual(self.sol.minDeletionSize(["cba", "daf", "ghi"]), 1)

    def test_multiple2(self):
        self.assertEqual(self.sol.minDeletionSize(["zyx", "wvu", "tsr"]), 3)


if __name__ == "__main__":
    unittest.main()
