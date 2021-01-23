from typing import List, Iterator, Tuple


class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        def start_positions() -> Iterator[Tuple[int, int]]:
            for row in range(rows):
                yield row, 0

            for col in range(1, cols):
                yield 0, col

        def read_array(row: int, col: int) -> List[int]:
            result = [matrix[row][col]]

            while 0 <= row + 1 < rows and 0 <= col + 1 < cols:
                row += 1
                col += 1

                result.append(matrix[row][col])

            return result

        def write_array(row: int, col: int, array: List[int]) -> None:
            pos = 0
            matrix[row][col] = array[pos]

            while 0 <= row + 1 < rows and 0 <= col + 1 < cols:
                row += 1
                col += 1
                pos += 1

                matrix[row][col] = array[pos]

        for row, col in start_positions():
            array = read_array(row, col)
            array.sort()
            write_array(row, col, array)

        return matrix
