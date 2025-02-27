class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        diag_pos_set = set()
        diag_neg_set = set()
        cols_set = set()

        board = [[False] * n for _ in range(n)]
        result = []

        def place_queen(row: int) -> None:
            if row == n:
                result.append(
                    ["".join("Q" if c else "." for c in row) for row in board]
                )
                return

            for col in range(n):
                if not (
                    row + col in diag_pos_set
                    or row - col in diag_neg_set
                    or col in cols_set
                ):
                    diag_pos_set.add(row + col)
                    diag_neg_set.add(row - col)
                    cols_set.add(col)

                    board[row][col] = True

                    place_queen(row + 1)

                    diag_pos_set.discard(row + col)
                    diag_neg_set.discard(row - col)
                    cols_set.discard(col)

                    board[row][col] = False

        place_queen(0)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.solveNQueens(4) == [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]
