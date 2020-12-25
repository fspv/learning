from typing import Tuple


def next_state(
    row: int, col: int, vector_row: int, vector_col: int, rows: int, cols: int
) -> Tuple[int, int, int, int]:
    next_row, next_col = row + vector_row, col + vector_col

    if not (0 <= next_row < rows) and not (0 <= next_col < cols):
        if (vector_row, vector_col) == (-1, 1):
            return row + 1, col, -vector_row, -vector_col
        else:
            return row, col + 1, -vector_row, -vector_col
    elif not (0 <= next_row < rows):
        return row, col + 1, -vector_row, -vector_col
    elif not (0 <= next_col < cols):
        return row + 1, col, -vector_row, -vector_col

    return next_row, next_col, vector_row, vector_col


def diagonal_traverse(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    vector_row, vector_col = -1, 1
    row, col = 0, 0

    result: List[int] = []

    while (row, col) != (rows - 1, cols - 1):
        result.append(matrix[row][col])
        row, col, vector_row, vector_col = next_state(
            row, col, vector_row, vector_col, rows, cols
        )

    result.append(matrix[row][col])

    return result


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        return diagonal_traverse(matrix)
