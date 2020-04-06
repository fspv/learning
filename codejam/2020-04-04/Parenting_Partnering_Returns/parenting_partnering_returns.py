import sys
from typing import Iterator, Tuple, Optional


def solution(intervals: Iterator[Tuple[int, int]]) -> Optional[list]:
    intervals_list = list(intervals)
    prev_ends = {True: float("-inf"), False: float("-inf")}
    result = [None] * len(intervals_list)

    for pos, interval in sorted(enumerate(intervals_list), key=lambda x: x[1]):
        for assign_to in [True, False]:
            if interval[0] >= prev_ends[assign_to]:
                prev_ends[assign_to] = interval[1]
                result[pos] = assign_to
                break
        else:
            return None

    return result


def read_intervals(
    lines: Iterator[str], number_of_intervals: int
) -> Iterator[Tuple[int, int]]:
    for _ in range(number_of_intervals):
        begin, end = next(lines).split()
        yield int(begin), int(end)


def parse_input(lines: Iterator[str]) -> Iterator[Iterator[Tuple[int, int]]]:
    number_of_tests = int(next(lines))
    for _ in range(number_of_tests):
        yield read_intervals(lines, int(next(lines)))


def main():
    case = 1
    for intervals in parse_input(sys.stdin):
        assign_to = solution(intervals)
        if assign_to is not None:
            print(
                "Case #%s: %s" % (
                    case, "".join("C" if t else "J" for t in assign_to)
                )
            )
        else:
            print("Case #%s: IMPOSSIBLE" % (case))
        case += 1


if __name__ == "__main__":
    main()
