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


def read_str() -> str:
    return sys.stdin.readline()


def main() -> None:
    string_len = read_int()
    string = read_str().strip()

    assert (
        len(string) == string_len
    ), f"{string} length is {len(string)}, shoud be {string_len}"

    result: List[str] = []

    space = False

    for char in string:
        if char == "*":
            space = True
        else:
            if space:
                result.append(" ")
                space = False

            result.append(char)

    print("".join(result))


if __name__ == "__main__":
    main()
