from typing import List, Iterator, Tuple


def neighbors(row: int, col: int, rows: int, cols: int) -> Iterator[Tuple[int, int]]:
    for neigh_row, neigh_col in (
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ):
        if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
            yield neigh_row, neigh_col


def longest_increasing_path_top_down(matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    longest_path = 0

    @lru_cache(None)
    def dp(row: int, col: int) -> int:
        max_length = 1

        for neigh_row, neigh_col in neighbors(row, col, rows, cols):
            if matrix[neigh_row][neigh_col] > matrix[row][col]:
                max_length = max(max_length, dp(neigh_row, neigh_col) + 1)

        return max_length

    for row in range(rows):
        for col in range(cols):
            longest_path = max(longest_path, dp(row, col))

    return longest_path


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0]) if matrix else 0

    dp = [[1] * cols for _ in range(rows)]

    for (row, col) in sorted(
        ((row, col) for row in range(rows) for col in range(cols)),
        key=lambda coord: -matrix[coord[0]][coord[1]],
    ):
        for neigh_row, neigh_col in neighbors(row, col, rows, cols):
            if matrix[neigh_row][neigh_col] > matrix[row][col]:
                dp[row][col] = max(dp[neigh_row][neigh_col] + 1, dp[row][col])

    return max(map(max, dp))


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return longest_increasing_path(matrix)
