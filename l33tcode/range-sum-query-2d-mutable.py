from typing import List


def next_power_of_two(num: int) -> int:
    if num == 0:
        return 0

    power = 1

    while num > power:
        power *= 2

    return power


def build_range_sum_col(array: List[int]) -> List[int]:
    length = next_power_of_two(len(array))
    result = [0 for _ in range(2 * length - 1)]

    for pos in range(length - 1, length * 2 - 1):
        if pos < length - 1 + len(array):
            result[pos] = array[pos - (length - 1)]
        else:
            result[pos] = 0

    for pos in reversed(range(length - 1)):
        result[pos] = result[2 * pos + 1] + result[2 * pos + 2]

    return result


def build_range_sum(matrix: List[List[int]]) -> List[List[int]]:
    length = next_power_of_two(len(matrix))
    result = [[0] for _ in range(2 * length - 1)]

    for pos in range(length - 1, length * 2 - 1):
        if pos < length - 1 + len(matrix):
            result[pos] = build_range_sum_col(matrix[pos - (length - 1)])
        else:
            result[pos] = build_range_sum_col([0] * len(matrix[0]))

    for pos in reversed(range(length - 1)):
        result[pos] = list(map(sum, zip(result[2 * pos + 1], result[2 * pos + 2])))

    return result


def update_range_sum_col(range_sums: List[int], col: int, diff: int) -> None:
    def dfs(range_sum: int, left_col: int, right_col: int, col: int, diff: int) -> None:
        range_sums[range_sum] += diff

        if right_col - left_col <= 1:
            return

        middle_col = (left_col + right_col) // 2

        if middle_col <= col:
            dfs(2 * range_sum + 2, middle_col, right_col, col, diff)
        else:
            dfs(2 * range_sum + 1, left_col, middle_col, col, diff)

    dfs(0, 0, (len(range_sums) + 1) // 2, col, diff)


def range_sum_col(range_sums: List[int], left_col: int, right_col: int) -> int:
    def dfs(
        range_sum: int,
        left_col_range: int,
        right_col_range: int,
        left_col: int,
        right_col: int,
    ) -> int:
        if (
            left_col <= left_col_range <= right_col
            and left_col <= right_col_range <= right_col
        ):
            return range_sums[range_sum]

        result = 0

        middle_col_range = (left_col_range + right_col_range) // 2

        if left_col < middle_col_range < right_col:
            result += dfs(
                range_sum * 2 + 1, left_col_range, middle_col_range, left_col, right_col
            )
            result += dfs(
                range_sum * 2 + 2,
                middle_col_range,
                right_col_range,
                left_col,
                right_col,
            )
        elif middle_col_range <= left_col:
            result += dfs(
                range_sum * 2 + 2,
                middle_col_range,
                right_col_range,
                left_col,
                right_col,
            )
        else:
            result += dfs(
                range_sum * 2 + 1, left_col_range, middle_col_range, left_col, right_col
            )

        return result

    return dfs(0, 0, (len(range_sums) + 1) // 2, left_col, right_col)


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self._range_sum = build_range_sum(matrix)
        self._matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        def dfs(
            range_sum: int, bottom_row: int, top_row: int, row: int, col: int, diff: int
        ) -> None:
            update_range_sum_col(self._range_sum[range_sum], col, diff)

            if top_row - bottom_row <= 1:
                return

            middle_row = (bottom_row + top_row) // 2

            if middle_row <= row:
                dfs(2 * range_sum + 2, middle_row, top_row, row, col, diff)
            else:
                dfs(2 * range_sum + 1, bottom_row, middle_row, row, col, diff)

        dfs(
            0,
            0,
            (len(self._range_sum) + 1) // 2,
            row,
            col,
            val - self._matrix[row][col],
        )
        self._matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def dfs(
            range_sum: int,
            bottom_row_range: int,
            top_row_range: int,
            left_col: int,
            right_col: int,
            bottom_row: int,
            top_row: int,
        ) -> int:
            # bottom_row_range, top_row_range - current row boundaries
            # left_col, right_col, bottom_row, top_row - what we're looking for
            if (
                bottom_row <= bottom_row_range <= top_row
                and bottom_row <= top_row_range <= top_row
            ):
                return range_sum_col(self._range_sum[range_sum], left_col, right_col)

            result = 0

            middle_row_range = (bottom_row_range + top_row_range) // 2

            if bottom_row < middle_row_range < top_row:
                result += dfs(
                    2 * range_sum + 1,
                    bottom_row_range,
                    middle_row_range,
                    left_col,
                    right_col,
                    bottom_row,
                    top_row,
                )
                result += dfs(
                    2 * range_sum + 2,
                    middle_row_range,
                    top_row_range,
                    left_col,
                    right_col,
                    bottom_row,
                    top_row,
                )
            elif middle_row_range <= bottom_row:
                result += dfs(
                    2 * range_sum + 2,
                    middle_row_range,
                    top_row_range,
                    left_col,
                    right_col,
                    bottom_row,
                    top_row,
                )
            else:
                result += dfs(
                    2 * range_sum + 1,
                    bottom_row_range,
                    middle_row_range,
                    left_col,
                    right_col,
                    bottom_row,
                    top_row,
                )

            return result

        return dfs(
            0, 0, (len(self._range_sum) + 1) // 2, col1, col2 + 1, row1, row2 + 1
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


class TestSolution:
    def test_case1(self) -> None:
        matrix = NumMatrix(
            [
                [3, 0, 1, 4, 2],
                [5, 6, 3, 2, 1],
                [1, 2, 0, 1, 5],
                [4, 1, 0, 1, 7],
                [1, 0, 3, 0, 5],
            ]
        )

        assert matrix.sumRegion(2, 1, 4, 3) == 8
        matrix.update(3, 2, 2)
        assert matrix.sumRegion(2, 1, 4, 3) == 10

    def test_case2(self) -> None:
        matrix = NumMatrix([[],])

    def test_case3(self) -> None:
        matrix = NumMatrix([[1],])

        assert matrix.sumRegion(0, 0, 0, 0) == 1
        matrix.update(0, 0, -1)
        assert matrix.sumRegion(0, 0, 0, 0) == -1
