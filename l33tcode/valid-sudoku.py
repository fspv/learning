import unittest

class Solution:
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        empty = "."

        rows = [set() for _ in range(len(board))]
        columns = [set() for _ in range(len(board[0]))]
        sub_boxes = [
            set() for _ in range(len(board)) for _ in range(len(board[0]))
        ]

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == empty:
                    continue

                if board[x][y] in rows[x]:
                    print(1)
                    print(rows)
                    print(x)
                    print(y)
                    print(board[x][y])
                    return False
                else:
                    rows[x].add(board[x][y])

                if board[x][y] in columns[y]:
                    print(2)
                    return False
                else:
                    columns[y].add(board[x][y])

                box_num = x // 3 * len(board[0]) // 3 + y // 3
                if board[x][y] in sub_boxes[box_num]:
                    print(3)
                    return False
                else:
                    sub_boxes[box_num].add(board[x][y])

        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        empty = "."

        rows = {k: set() for k in range(len(board))}
        columns = {k: set() for k in range(len(board[0]))}
        sub_boxes = {(x, y): set() for x in range(0, 3) for y in range(0, 3)}

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == empty:
                    continue

                if board[x][y] in rows[x]:
                    return False
                else:
                    rows[x].add(board[x][y])

                if board[x][y] in columns[y]:
                    return False
                else:
                    columns[y].add(board[x][y])

                if board[x][y] in sub_boxes[(x // 3, y // 3)]:
                    return False
                else:
                    sub_boxes[(x // 3, y // 3)].add(board[x][y])

        return True

    def isValidSudoku3it(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        empty = "."

        # Check 1st rule
        for x in range(len(board)):
            row = set()
            for y in range(len(board[0])):
                if board[x][y] == empty:
                    continue
                if board[x][y] in row:
                    return False
                else:
                    row.add(board[x][y])

        # Check 2nd rule
        for y in range(len(board[0])):
            column = set()
            for x in range(len(board)):
                if board[x][y] == empty:
                    continue
                if board[x][y] in column:
                    return False
                else:
                    column.add(board[x][y])

        # Check 3rd rule
        sub_boxes = 3
        sub_box_step_x = int(len(board) / sub_boxes)
        sub_box_step_y = int(len(board) / sub_boxes)
        for sub_x in range(0, len(board), sub_box_step_x):
            for sub_y in range(0, len(board[0]), sub_box_step_y):
                sub_box = set()
                for x in range(sub_x, sub_x + sub_box_step_x):
                    for y in range(sub_y, sub_y + sub_box_step_y):
                        if board[x][y] == empty:
                            continue
                        if board[x][y] in sub_box:
                            return False
                        else:
                            sub_box.add(board[x][y])

        return True


class Tests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        self.assertTrue(self.sol.isValidSudoku([["."] * 9] * 9))
        self.assertTrue(
            self.sol.isValidSudoku(
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )
        self.assertFalse(
            self.sol.isValidSudoku(
                [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )


unittest.main()
