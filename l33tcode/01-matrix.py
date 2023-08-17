import unittest
from typing import List, Set, Tuple


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0
        dp = [
            [rows * cols if matrix[row][col] else 0 for col in range(cols)]
            for row in range(rows)
        ]

        # Top-down, left-right
        for row in range(rows):
            for col in range(cols):
                if col > 0:
                    dp[row][col] = min(dp[row][col], dp[row][col - 1] + 1)
                if row > 0:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col] + 1)

        # Bottom-up, right-left
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if col < cols - 1:
                    dp[row][col] = min(dp[row][col], dp[row][col + 1] + 1)
                if row < rows - 1:
                    dp[row][col] = min(dp[row][col], dp[row + 1][col] + 1)

        return dp

    def updateMatrixBFS(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    continue

                stack = [(y, x)]
                visited: Set[Tuple[int, int]] = set()
                level = 1

                while stack:
                    stack_old = stack
                    stack: List[Tuple[int, int]] = []
                    for new_y, new_x in stack_old:
                        visited.add((new_y, new_x))

                        for tmp_y, tmp_x in [
                            (new_y, new_x + 1),
                            (new_y, new_x - 1),
                            (new_y + 1, new_x),
                            (new_y - 1, new_x),
                        ]:
                            if (
                                0 <= tmp_y < len(matrix)
                                and 0 <= tmp_x < len(matrix[0])
                                and not (tmp_y, tmp_x) in visited
                            ):
                                if matrix[tmp_y][tmp_x] == 0:
                                    output[y][x] = level
                                    break
                                else:
                                    stack.append((tmp_y, tmp_x))
                        else:
                            continue
                        break
                    else:
                        level += 1
                        continue

                    break

        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_element(self):
        self.assertListEqual(self.sol.updateMatrix([[0]]), [[0]])

    def test_two_element(self):
        self.assertListEqual(self.sol.updateMatrix([[0], [0]]), [[0], [0]])

    def test_two_element_2(self):
        self.assertListEqual(self.sol.updateMatrix([[0, 0]]), [[0, 0]])

    def test_two_element_3(self):
        self.assertListEqual(self.sol.updateMatrix([[0, 1]]), [[0, 1]])

    def test_case1(self):
        self.assertListEqual(
            self.sol.updateMatrix([[0, 1, 1], [1, 1, 1], [1, 1, 1]]),
            [[0, 1, 2], [1, 2, 3], [2, 3, 4]],
        )

    def test_case2(self):
        self.assertListEqual(
            self.sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
        )

    def test_case3(self):
        self.assertListEqual(
            self.sol.updateMatrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        )

    def test_case4(self):
        self.assertListEqual(
            self.sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        )


if __name__ == "__main__":
    unittest.main()
