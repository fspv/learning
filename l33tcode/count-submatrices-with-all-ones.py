from typing import List


def matrices_in_rect(rows: int, cols: int) -> int:
    return int((cols * (cols + 1) / 2) * (rows * (rows + 1) / 2))


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def count_rectangles(start_row: int, start_col: int) -> int:
            rows, cols = len(mat), len(mat[0]) if mat else 0
            count = 0

            max_col = cols

            for row in range(start_row, rows):
                if mat[row][start_col] != 1:
                    break

                for col in range(start_col, max_col):
                    if mat[row][col] != 1:
                        break

                    max_col = col + 1
                    count += 1

            return count

        rows, cols = len(mat), len(mat[0]) if mat else 0
        count = 0
        for row in range(rows):
            for col in range(cols):
                count += count_rectangles(row, col)

        return count

    def numSubmat1(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0]) if mat else 0
        sizes = [[(0, 0)] * (cols + 1) for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    sizes[row + 1][col + 1] = (
                        min(sizes[row][col + 1][0], sizes[row][col][0]) + 1,
                        min(sizes[row + 1][col][1], sizes[row][col][1]) + 1,
                    )

        print(sizes)
        return 0
