# /usr/bin/env python3

import sys
from typing import List, Tuple, Iterator


def update_reachability(
    matrix: List[List[bool]],
    incoming_allowed: List[bool],
    outgoing_allowed: List[bool],
    src: int,
    dst: int,
) -> None:
    prev_src, prev_dst = src - 1, dst - 1
    # Can we get from src to prev dst
    to_prev_dst = matrix[src][prev_dst] if prev_dst >= 0 else False
    # Can we get from prev src to dst
    from_prev_src = matrix[prev_src][dst] if prev_src >= 0 else False

    if src == dst:
        # Same airport
        matrix[src][dst] = True
    elif to_prev_dst and outgoing_allowed[prev_dst] and incoming_allowed[dst]:
        """
        * we can get from src to previous airport
        * we can get from the previous airport to this one
        * we allow incoming flights to this airport
        """
        matrix[src][dst] = True
    elif from_prev_src and outgoing_allowed[src] and incoming_allowed[prev_src]:
        """
        * we can get from previous src to the dst
        * we can get from this airport to the previous src
        * we allow incoming flights on the previous src
        """
        matrix[src][dst] = True
    else:
        matrix[src][dst] = False


def calculate_reachability(
    matrix: List[List[bool]], incoming_allowed: List[bool], outgoing_allowed: List[bool]
) -> None:
    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    for src in range(rows):
        for dst in range(cols):
            update_reachability(matrix, incoming_allowed, outgoing_allowed, src, dst)


def create_matrix(size: int) -> List[List[bool]]:
    return [[False] * size for _ in range(size)]


def read_number_of_airlines(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_airline(lines: Iterator[str]) -> Tuple[int, List[bool], List[bool]]:
    countries = int(next(lines))
    incoming_allowed = list(map(lambda x: x == "Y", list(next(lines))))
    outgoing_allowed = list(map(lambda x: x == "Y", list(next(lines))))

    return countries, incoming_allowed, outgoing_allowed


def read_airlines(lines: Iterator[str]) -> Iterator[Tuple[int, List[bool], List[bool]]]:
    number_of_tests = read_number_of_airlines(lines)

    for _ in range(number_of_tests):
        yield read_airline(lines)


def print_answer(case: int, matrix: List[List[bool]]) -> None:
    print(f"Case #{case}:")
    for line in matrix:
        output = "".join(map(lambda x: "Y" if x else "N", line))
        print(output)


def main() -> None:
    case = 1
    for countries, incoming_allowed, outgoing_allowed in read_airlines(sys.stdin):
        matrix = create_matrix(countries)
        calculate_reachability(matrix, incoming_allowed, outgoing_allowed)
        print_answer(case, matrix)
        case += 1


if __name__ == "__main__":
    main()
