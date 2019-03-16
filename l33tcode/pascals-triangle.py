import unittest

class Solution:
    def generate(self, numRows):
        result = []

        for level in range(numRows):
            result.append([])

            for pos in range(level + 1):
                if pos == 0 or pos == level:
                    result[level].append(1)
                else:
                    result[level].append(
                        result[level - 1][pos - 1] + result[level - 1][pos]
                    )

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        assert self.sol.generate(0) == []

    def test_one(self):
        assert self.sol.generate(1) == [[1]]

    def test_two(self):
        assert self.sol.generate(2) == [[1], [1, 1]]

    def test_three(self):
        assert self.sol.generate(3) == [
            [1],
            [1, 1],
            [1, 2, 1],
        ]

    def test_four(self):
        assert self.sol.generate(4) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
        ]

    def test_five(self):
        assert self.sol.generate(5) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]

    def test_six(self):
        assert self.sol.generate(6) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
        ]


if __name__ == "__main__":
    unittest.main()
