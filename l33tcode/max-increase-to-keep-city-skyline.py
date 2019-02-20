import unittest


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        rows_max =  [0] * len(grid)
        columns_max =  [0] * len(grid[0])

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if rows_max[row] < grid[row][column]:
                    rows_max[row] = grid[row][column]
                if columns_max[column] < grid[row][column]:
                    columns_max[column] = grid[row][column]

        result = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                result += \
                    min(rows_max[row], columns_max[column]) - grid[row][column]

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1x1(self):
        self.assertEqual(
            self.sol.maxIncreaseKeepingSkyline([[1]]),
            0,
        )

    def test_2x2(self):
        self.assertEqual(
            self.sol.maxIncreaseKeepingSkyline([[1, 2], [3, 4]]),
            1,
        )

    def test_custom(self):
        self.assertEqual(
            self.sol.maxIncreaseKeepingSkyline(
                [
                    [3, 0, 8, 4],
                    [2, 4, 5, 7],
                    [9, 2, 6, 3],
                    [0, 3, 1, 0],
                ]
            ),
            35,
        )


if __name__ == "__main__":
    unittest.main()
