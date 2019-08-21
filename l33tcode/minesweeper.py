from functools import lru_cache


class Solution:
    def updateBoard(self, board, click):
        row, col = click[0], click[1]

        if board[row][col] == "M":
            board[row][col] = "X"
            return board

        def cells_around(row, col):
            for cur_row, cur_col in [
                    (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1), (row, col + 1),
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
            ]:
                if 0 <= cur_row < len(board) and 0 <= cur_col < len(board[0]):
                    yield cur_row, cur_col

        @lru_cache(None)
        def backtrack(row, col):
            mines = sum(
                [
                    1 for cur_row, cur_col in cells_around(row, col) \
                    if board[cur_row][cur_col] == "M"
                ]
            )

            if mines > 0:
                board[row][col] = str(mines)
            elif board[row][col] != "B": # Initial cell is not in lru_cache till the end
                board[row][col] = "B"
                for cur_row, cur_col in cells_around(row, col):
                    backtrack(cur_row, cur_col)

        backtrack(row, col)

        return board



class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_two(self):
        assert self.sol.updateBoard([['M']], [0, 0]) == [['X']]
        assert self.sol.updateBoard([['E']], [0, 0]) == [['B']]

    def test_three(self):
        assert self.sol.updateBoard([['M', 'E']], [0, 0]) == [['X', 'E']]
        assert self.sol.updateBoard([['E', 'E']], [0, 0]) == [['B', 'B']]
        assert self.sol.updateBoard([['E', 'M']], [0, 0]) == [['1', 'M']]

    def test_one(self):
        assert self.sol.updateBoard(
            [
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'M', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
            ],
            [3, 0],
        ) == [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B'],
        ]

    def test_four(self):
        assert self.sol.updateBoard(
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ],
            [1, 2],
        ) == [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'X', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']
        ]
