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


def can_sell(requests: List[int], max_sugar: int, total_sugar: int) -> bool:
    left_sugar = total_sugar

    for request in requests:
        will_give = min(request, max_sugar)

        if will_give <= left_sugar:
            left_sugar -= will_give
        else:
            return False

    return True


def max_sugar(requests: List[int], total_sugar: int) -> int:
    left, right = 0, total_sugar + 1

    while left < right:
        mid = left + (right - left) // 2
        if not can_sell(requests, mid, total_sugar):
            right = mid
        else:
            left = mid + 1

    return left - 1


def main() -> None:
    customers, total_sugar = read_list_int(2)

    requests = read_list_int(customers)

    print(max_sugar(requests, total_sugar))


if __name__ == "__main__":
    main()
