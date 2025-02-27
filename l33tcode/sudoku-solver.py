import heapq


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        row_constraints = [set() for _ in range(rows)]
        col_constraints = [set() for _ in range(cols)]
        box_constraints = [set() for _ in range((rows * cols) // 9)]
        box_left = [rows for _ in range((rows * cols) // 9)]

        boxes = [(l, b) for b, l in enumerate(box_left)]
        heapq.heapify(boxes)

        def init_constraints() -> None:
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] != ".":
                        box = 3 * (row // 3) + col // 3
                        set_number(box, row, col, board[row][col])

        def set_number(box: int, row: int, col: int, num: str) -> bool:
            if num in row_constraints[row]:
                return False
            if num in col_constraints[col]:
                return False
            if num in box_constraints[box]:
                return False

            row_constraints[row].add(num)
            col_constraints[col].add(num)
            box_constraints[box].add(num)
            box_left[box] -= 1

            board[row][col] = num
            return True

        def unset_number(box: int, row: int, col: int, num: str) -> None:
            row_constraints[row].remove(num)
            col_constraints[col].remove(num)
            box_constraints[box].remove(num)
            box_left[box] += 1
            board[row][col] = "."

        def next_cell(box: int, row: int, col: int) -> tuple[int, int]:
            row_offset, col_offset = box_first(box)
            row_shift, col_shift = row - row_offset, col - col_offset

            tmp = 3 * row_shift + col_shift + 1
            row_tmp = tmp // 3
            col_tmp = tmp % 3

            return row_offset + row_tmp, col_offset + col_tmp

        def box_first(box: int) -> tuple[int, int]:
            col = (box % 3) * 3
            row = (box // 3) * 3

            return row, col

        def fill(box: int) -> bool:
            if sum(box_left) == 0:
                return True

            row, col = box_first(box)

            return fill_box(box, row, col)

        def fill_box(box: int, row: int, col: int) -> bool:
            if box_left[box] == 0:
                if not boxes:
                    return True
                l, next_box = heapq.heappop(boxes)
                if fill(next_box):
                    return True
                heapq.heappush(boxes, (l, next_box))
                return False

            next_row, next_col = next_cell(box, row, col)

            if board[row][col] != ".":
                return fill_box(box, next_row, next_col)

            for num in range(1, 10):
                if set_number(box, row, col, str(num)):
                    if fill_box(box, next_row, next_col):
                        return True
                    unset_number(box, row, col, str(num))

            return False

        init_constraints()
        fill(heapq.heappop(boxes)[1])


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        self.sol.solveSudoku(
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
