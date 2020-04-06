import sys
from functools import lru_cache
from typing import Iterator, Tuple, Optional, List, Set, Dict


def find_possible_sums(target: int, max_diff: int, steps: int):
    @lru_cache(None)
    def dfs(target_left: int, max_diff: int, steps_left: int):
        if target_left < 0:
            return

        if target_left > 0 and steps_left == 0:
            return

        if target_left == 0 and steps_left == 0:
            return [[]]

        if target_left // steps_left > max_diff:
            return

        result = []

        for diff in reversed(range(1, max_diff + 1)):
            sums = dfs(target_left - diff, max_diff, steps_left - 1)

            for s in sums if sums else []:
                result.append([diff] + s)

        return result

    return dfs(target, max_diff, steps)


def find_possible_fill(size: int, traces: List[List[int]]) -> Optional[List[List[int]]]:
    def dfs(
        row: int,
        col: int,
        size: int,
        visited: List[List[bool]],
        matrix: List[List[int]],
        row_cache: List[Set[int]],
        col_cache: List[Set[int]],
    ) -> bool:
        for num in [matrix[row][col]] if row == col else range(1, size + 1):
            if num in row_cache[row] or num in col_cache[col]:
                continue

            matrix[row][col] = num
            visited[row][col] = True
            row_cache[row].add(num)
            col_cache[col].add(num)

            leaf_node = True
            paths_valid = True

            for row_next, col_next in [
                (row, col + 1),
                (row, col - 1),
                (row - 1, col),
                (row + 1, col),
            ]:
                if (
                    0 <= row_next < len(matrix)
                    and 0 <= col_next < len(matrix[0])
                    and not visited[row_next][col_next]
                ):
                    leaf_node = False
                    if not dfs(
                        row_next, col_next, size, visited, matrix, row_cache, col_cache
                    ):
                        paths_valid = False
                        break

            if leaf_node:
                return True

            if paths_valid:
                return True

            visited[row][col] = False
            row_cache[row].remove(num)
            col_cache[col].remove(num)

        return False

    for trace in traces:
        matrix = [[0] * size for _ in range(size)]
        visited = [[False] * size for _ in range(size)]

        row_cache = [set() for _ in range(size)]
        col_cache = [set() for _ in range(size)]
        for pos in range(size):
            matrix[pos][pos] = trace[pos]

        if dfs(0, 0, size, visited, matrix, row_cache, col_cache):
            return matrix

    return None


def solution(size: int, trace: int):
    traces = find_possible_sums(trace, size, size)
    return find_possible_fill(size, traces)


def parse_input(lines: Iterator[str]) -> Iterator[Tuple[int, int]]:
    number_of_tests = int(next(lines))
    for _ in range(number_of_tests):
        size, trace = next(lines).split()
        yield int(size), int(trace)


def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    case = 1
    for size, trace in parse_input(sys.stdin):
        matrix = solution(size, trace)

        print("Case #%s: %s" % (case, "POSSIBLE" if matrix else "IMPOSSIBLE"))
        if matrix:
            print_matrix(matrix)

        case += 1


if __name__ == "__main__":
    main()
