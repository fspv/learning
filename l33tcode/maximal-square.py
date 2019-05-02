class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        dp = [
            [0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)
        ]

        result = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    continue
                dp[row + 1][col + 1] = min(
                    dp[row][col + 1],
                    dp[row + 1][col],
                    dp[row][col],
                ) + 1
                result = max(result, dp[row + 1][col + 1])

        return result ** 2

    def maximalSquareBruteForce(self, matrix):
        # Not finished, too complicated
        cache = [
            [(0, 0) for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        ]

        def find_square(row, col, size):
            for new_col in range(col, col + size + 1):
                if size > cache[row][col][0] and matrix[row + size][new_col] == "0":
                    return size
            for new_row in range(row, row + size + 1):
                if size > cache[row][col][1] and matrix[new_row][col + size] == "0":
                    return size

            max_size = find_square(row, col, size + 1)

            for new_col in range(col, col + size + 1):
                cache[row + size][new_col] = (
                    max_size - size,
                    max_size - ( new_col - col),
                )

            for new_row in range(row, row + size):
                cache[new_row][col + size] = (
                    max_size - (new_row - row),
                    max_size - size,
                )

            return max_size


        result = 0
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                result = max(result, find_square(row, col, min(cache[row][col])))

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.maximalSquare(
            [
                ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"],
            ]
        ) == 4

    def test_custom2(self):
        assert self.sol.maximalSquare(
            [
                ["0","0","0","1"],
                ["1","1","0","1"],
                ["1","1","1","1"],
                ["0","1","1","1"],
                ["0","1","1","1"],
            ]
        ) == 9

    def test_custom3(self):
        assert self.sol.maximalSquare(
            [
                ["1","0","1","0","0","1","1","1","0"],
                ["1","1","1","0","0","0","0","0","1"],
                ["0","0","1","1","0","0","0","1","1"],
                ["0","1","1","0","0","1","0","0","1"],
                ["1","1","0","1","1","0","0","1","0"],
                ["0","1","1","1","1","1","1","0","1"],
                ["1","0","1","1","1","0","0","1","0"],
                ["1","1","1","0","1","0","0","0","1"],
                ["0","1","1","1","1","0","0","1","0"],
                ["1","0","0","1","1","1","0","0","0"],
            ]
        ) == 4
