import unittest


class Solution:
    def largestOverlap(self, A, B):
        max_overlap = 0
        for row_offset in range(- len(A) + 1, len(A)):
            for col_offset in range(- len(A) + 1, len(A)):
                overlap = 0
                for A_row in range(
                    max(0, row_offset),
                    min(len(A), len(A) + row_offset)
                ):
                    for A_col in range(
                        max(0, col_offset),
                        min(len(A), len(A) + col_offset)
                    ):
                        if A[A_row][A_col] and \
                           B[A_row - row_offset][A_col - col_offset]:
                            overlap += 1
                max_overlap = max(overlap, max_overlap)
        return max_overlap


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.largestOverlap([], []), 0)

    def test_one1(self):
        self.assertEqual(self.sol.largestOverlap([[0]], [[0]]), 0)

    def test_one2(self):
        self.assertEqual(self.sol.largestOverlap([[1]], [[0]]), 0)

    def test_one3(self):
        self.assertEqual(self.sol.largestOverlap([[1]], [[1]]), 1)

    def test_four(self):
        self.assertEqual(self.sol.largestOverlap([[0,1], [0, 0]], [[1,0], [0, 0]]), 1)

    def test_custom1(self):
        self.assertEqual(
            self.sol.largestOverlap(
                [[1,1,0],
                [0,1,0],
                [0,1,0]],
                [[0,0,0],
                [0,1,1],
                [0,0,1]],
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
