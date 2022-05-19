import sys
from typing import List, Set, Tuple


def read_int() -> int:
    return int(sys.stdin.readline())


def read_list_int(length: int) -> List[int]:
    result = list(map(int, sys.stdin.readline().split()))

    assert (
        len(result) == length
    ), f"List must of of length of {length}, but got {result}"

    return result


def read_str() -> str:
    return sys.stdin.readline()


def new_elements(left: List[int], right: List[int]) -> Tuple[int, int]:
    min_left_pos, max_left_pos = (
        min(range(len(left)), key=lambda x: left[x]),
        max(range(len(left)), key=lambda x: left[x]),
    )
    min_right_pos, max_right_pos = (
        min(range(len(right)), key=lambda x: right[x]),
        max(range(len(right)), key=lambda x: right[x]),
    )

    min_left, max_left = left[min_left_pos], left[max_left_pos]
    min_right, max_right = right[min_right_pos], right[max_right_pos]

    if max_left > 0 and max_right > 0:
        return max_left_pos + 1, max_right_pos + 1
    elif min_left < 0 and min_right < 0:
        return min_left_pos + 1, min_right_pos + 1
    else:
        sign = 1 if max_left <= min_right else -1
        existing_items: Set[int] = set(left) | set(right)

        for left_pos, left_item in sorted(enumerate(left), key=lambda x: - sign * x[1]):
            for right_pos, right_item in sorted(enumerate(right), key=lambda x: sign * x[1]):
                if left_item + right_item not in existing_items:
                    return left_pos + 1, right_pos + 1


def main() -> None:
    left_count, right_count = read_list_int(2)

    left = read_list_int(left_count)
    right = read_list_int(right_count)

    print(" ".join(map(str, new_elements(left, right))))


if __name__ == "__main__":
    main()
