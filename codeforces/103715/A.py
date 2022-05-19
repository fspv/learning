import sys
from typing import List


def read_int() -> int:
    return int(sys.stdin.readline())


def read_list_int(length: int) -> List[int]:
    result = list(map(int, sys.stdin.readline().split()))

    assert (
        len(result) == length
    ), f"List must of of length of {length}, but got {result}"

    return result


def main() -> None:
    x, y, t1, t2 = read_list_int(4)

    print(x * t1 + y * t2)


if __name__ == "__main__":
    main()
