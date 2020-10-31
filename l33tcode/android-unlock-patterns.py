from typing import Iterator, Tuple, List
from functools import lru_cache

# 0 1 2
# 3 4 5
# 6 7 8

class Solution:
    def numberOfPatterns(self, min_length: int, max_length: int) -> int:
        def intersects(row: int, col: int, next_row: int, next_col: int) -> List[int]:
            start, end = list(sorted([row * 3 + col, next_row * 3 + next_col]))

            return {
                (0, 2): [1],
                (0, 5): [],
                (0, 8): [4],
                (0, 7): [],
                (0, 6): [3],
                (1, 6): [],
                (1, 7): [4],
                (1, 8): [],
                (2, 6): [4],
                (2, 7): [],
                (2, 8): [5],
                (2, 3): [],
                (3, 5): [4],
                (3, 8): [],
                (5, 6): [],
                (6, 8): [7],
            }[(start, end)]

        def neighbors(row: int, col: int, selected: int) -> Iterator[Tuple[int, int]]:
            for neigh_row in range(3):
                for neigh_col in range(3):
                    pos = neigh_row * 3 + neigh_col

                    if selected & (1 << pos) == 0:
                        if abs(neigh_row - row) <= 1 and abs(neigh_col - col) <= 1:
                            yield (neigh_row, neigh_col)
                        else:
                            if all(
                                selected & (1 << intersects_pos) > 0
                                for intersects_pos in intersects(
                                    row, col, neigh_row, neigh_col
                                )
                            ):
                                yield (neigh_row, neigh_col)

        @lru_cache(None)
        def dp(row: int, col: int, length: int, selected: int) -> int:
            count = 0

            if length > max_length:
                return count

            if length >= min_length:
                count += 1

            for neigh_row, neigh_col in neighbors(row, col, selected | 1 << (row * 3 + col)):
                count += dp(
                    neigh_row,
                    neigh_col,
                    length + 1,
                    selected | 1 << (neigh_row * 3 + neigh_col) | 1 << (row * 3 + col),
                )

            return count

        count = 0
        for row in range(3):
            for col in range(3):
                count += dp(row, col, 1, 0)

        return count
