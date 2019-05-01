class Solution:
    def countCornerRectangles(self, grid):
        result = 0

        row_cache = [
            set([col for col, val in enumerate(row) if val])
            for row in grid
        ]

        for row in range(len(grid)):
            for row_inner in row_cache[row + 1:]:
                common = len(row_inner & row_cache[row])
                result += common * (common - 1) // 2

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.countCornerRectangles([[1]]) == 0

    def test_custom1(self):
        assert self.sol.countCornerRectangles(
            [[1, 0, 0, 1, 0],
             [0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0],
             [1, 0, 1, 0, 1]]
        ) == 1

    def test_custom2(self):
        assert self.sol.countCornerRectangles(
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
        ) == 9

    def test_custom3(self):
        assert self.sol.countCornerRectangles(
            [[1, 1, 1, 1]]
        ) == 0
