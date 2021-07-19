#!/bin/python3
import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(square: List[List[int]]) -> int:
    rows, cols = len(square), len(square[0]) if square else 0
    magick_square = [[0] * cols for _ in range(rows)]

    max_value = rows * cols

    def validate() -> bool:
        cols_sums: List[int] = [0] * cols
        rows_sums: List[int] = [0] * rows
        diag1, diag2 = 0, 0

        for row in range(rows):
            for col in range(cols):
                cols_sums[col] += magick_square[row][col]
                rows_sums[row] += magick_square[row][col]
                if row == col:
                    diag1 += magick_square[row][col]
                if (cols - col - 1) == row:
                    diag2 += magick_square[row][col]

        # It is a square
        return (
            cols_sums == rows_sums
            and len(set(cols_sums)) == 1
            and cols_sums[0] == diag1 == diag2
        )

    def diff(left: List[List[int]], right: List[List[int]]) -> int:
        _diff = 0

        for row in range(rows):
            for col in range(cols):
                _diff += abs(left[row][col] - right[row][col])

        return _diff

    def backtrack(row: int, col: int, nums_set: int) -> int:
        min_cost = rows * cols * max_value

        if row == rows:
            if validate():
                return diff(magick_square, square)
            else:
                return min_cost

        next_col = (col + 1) % cols
        next_row = row if next_col > 0 else row + 1

        for new_value in range(1, max_value + 1):
            if nums_set & (1 << (new_value - 1)):
                continue

            magick_square[row][col] = new_value
            min_cost = min(
                min_cost,
                backtrack(next_row, next_col, nums_set | (1 << (new_value - 1))),
            )

        return min_cost

    return backtrack(0, 0, 0)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + "\n")

    fptr.close()
