import unittest
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            next_row = [1] + [0] * (len(row) - 1) + [1]
            for pos in range(1, len(next_row) - 1):
                next_row[pos] = row[pos - 1] + row[pos]

            row = next_row

        return row


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.getRow(0) == [1]

    def test_two(self):
        assert self.sol.getRow(1) == [1, 1]

    def test_three(self):
        assert self.sol.getRow(2) == [1, 2, 1]

    def test_four(self):
        assert self.sol.getRow(3) == [1, 3, 3, 1]

    def test_five(self):
        assert self.sol.getRow(4) == [1, 4, 6, 4, 1]

    def test_six(self):
        assert self.sol.getRow(5) == [1, 5, 10, 10, 5, 1]

    def test_six(self):
        assert self.sol.getRow(33) == [
            1,
            33,
            528,
            5456,
            40920,
            237336,
            1107568,
            4272048,
            13884156,
            38567100,
            92561040,
            193536720,
            354817320,
            573166440,
            818809200,
            1037158320,
            1166803110,
            1166803110,
            1037158320,
            818809200,
            573166440,
            354817320,
            193536720,
            92561040,
            38567100,
            13884156,
            4272048,
            1107568,
            237336,
            40920,
            5456,
            528,
            33,
            1,
        ]


if __name__ == "__main__":
    unittest.main()
