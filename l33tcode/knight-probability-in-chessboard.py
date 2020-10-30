from typing import Tuple, Iterator
from functools import lru_cache


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def check_within_the_board(row: int, col: int) -> bool:
            return 0 <= row < N and 0 <= col < N

        def moves(row: int, col: int) -> Iterator[Tuple[int, int]]:
            for next_row, next_col in (
                (row + 2, col - 1),
                (row + 2, col + 1),
                (row + 1, col - 2),
                (row + 1, col + 2),
                (row - 1, col - 2),
                (row - 1, col + 2),
                (row - 2, col - 1),
                (row - 2, col + 1),
            ):
                yield next_row, next_col

        @lru_cache(None)
        def dp(row: int, col: int, moves_left: int) -> Tuple[int, int]:
            if moves_left == 0:
                return (1, 0) if check_within_the_board(row, col) else (0, 1)

            if not check_within_the_board(row, col):
                return (0, 8 ** moves_left)

            inside_total, outside_total = 0, 0
            for next_row, next_col in moves(row, col):
                inside, outside = dp(next_row, next_col, moves_left - 1)
                inside_total += inside
                outside_total += outside

            return inside_total, outside_total

        inside, outside = dp(r, c, K)

        return inside / (inside + outside)
