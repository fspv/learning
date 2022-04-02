import sys
from typing import Iterator, List, Tuple


def solution(rows: int, cols: int) -> None:
    for row in range(rows * 2 + 1):
        data: List[str] = []
        for col in range(cols * 2 + 1):
            if (row, col) in {(0, 0), (0, 1), (1, 0)}:
                data.append(".")
            elif row % 2 == 0 and col % 2 == 0:
                data.append("+")
            elif row % 2 == 0 and col % 2 == 1:
                data.append("-")
            elif row % 2 == 1 and col % 2 == 0:
                data.append("|")
            elif row % 2 == 1 and col % 2 == 1:
                data.append(".")

        print("".join(data))


def read_2_integers(lines: Iterator[str]) -> Tuple[int, int]:
    begin, end = next(lines).split()
    return int(begin), int(end)


def parse_input(lines: Iterator[str]) -> Iterator[Tuple[int, int]]:
    number_of_tests = int(next(lines))
    for _ in range(number_of_tests):
        yield read_2_integers(lines)


def main():
    case = 1
    for rows, cols in parse_input(sys.stdin):
        # Prints data inside
        print(f"Case #{case}:")
        solution(rows, cols)
        case += 1


if __name__ == "__main__":
    main()
