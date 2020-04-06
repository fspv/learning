import sys
from typing import Iterator, List, Tuple


def read_matrix(lines: Iterator[str], size: int) -> Iterator[List[int]]:
    for _ in range(size):
        yield list(map(int, next(lines).split()))[:size]


def parse_input(lines: Iterator[str]) -> Iterator[Tuple[int, List[int]]]:
    number_of_tests = int(next(lines))

    for _ in range(number_of_tests):
        size = int(next(lines))
        yield size, read_matrix(lines, size)


def solution(size, matrix_iterator):
    trace = 0
    col_cache = [set() for _ in range(size)]
    row_rep, col_rep = [False] * size, [False] * size

    for row_num, row in enumerate(matrix_iterator):
        row_cache = set()
        for col_num in range(size):
            if row[col_num] in row_cache:
                row_rep[row_num] = True
            if row[col_num] in col_cache[col_num]:
                col_rep[col_num] = True

            row_cache.add(row[col_num])
            col_cache[col_num].add(row[col_num])

            if row_num == col_num:
                trace += row[col_num]

    return trace, row_rep.count(True), col_rep.count(True)


def main():
    case = 1
    for size, matrix_iterator in parse_input(sys.stdin):
        trace, row_rep, col_rep = solution(size, matrix_iterator)

        print("Case #%s: %s %s %s" % (case, trace, row_rep, col_rep))

        case += 1


if __name__ == "__main__":
    main()
