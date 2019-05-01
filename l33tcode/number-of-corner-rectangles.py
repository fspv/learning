class Solution:
    def countCornerRectangles(self, grid):
        count = 0
        row_cache = [list() for _ in range(len(grid))]
        col_cache = [set() for _ in range(len(grid[0]))]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    row_cache[row].append(col)
                    col_cache[col].add(row)

        for row in range(len(grid)):
            for lc_pos, lc in enumerate(row_cache[row]):
                for rc in row_cache[row][lc_pos + 1:]:
                    col_cache[lc].discard(row)
                    col_cache[rc].discard(row)

                    count += len(col_cache[lc].intersection(col_cache[rc]))

        return count


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
