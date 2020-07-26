# /usr/bin/env python3

import sys
from typing import List, Tuple, Dict, Iterator


def longest_combined_timber(heights: List[Tuple[int, int]]) -> int:
    # Longest combined timber that ends at the position
    longest_timber: Dict[int, int] = {}
    result = 0

    for pos, height in heights:
        longest_timber[pos + height] = max(
            longest_timber.get(pos + height, 0), longest_timber.get(pos, 0) + height,
        )
        longest_timber[pos] = max(
            longest_timber.get(pos, 0), height + longest_timber.get(pos - height, 0),
        )
        result = max(result, longest_timber[pos + height], longest_timber[pos],)

    return result


def read_number_of_sections(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_number_of_trees(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_position(lines: Iterator[str]) -> Tuple[int, int]:
    height_str, position_str = next(lines).split()
    return int(height_str), int(position_str)


def read_section(lines: Iterator[str]) -> List[Tuple[int, int]]:
    heights = []
    for _ in range(read_number_of_trees(lines)):
        heights.append(read_position(lines))

    heights.sort()

    return heights


def read_sections(lines: Iterator[str]) -> Iterator[List[Tuple[int, int]]]:
    for _ in range(read_number_of_sections(lines)):
        yield read_section(lines)


def print_answer(case: int, answer: int) -> None:
    print(f"Case #{case}: {answer}")


def main():
    case = 1
    for heights in read_sections(sys.stdin):
        answer = longest_combined_timber(heights)
        print_answer(case, answer)
        case += 1


if __name__ == "__main__":
    main()
