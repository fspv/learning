import sys
from collections import deque
from typing import Iterator


def solution(string: str) -> str:
    def add_parens(number: int) -> deque:
        result = deque([str(number)])
        for _ in range(number):
            result.appendleft("(")
            result.append(")")

        return result

    def fold_parens(queue_left, queue_right):
        if not queue_left:
            return queue_right

        while queue_left[-1] == ")" and queue_right[0] == "(":
            queue_left.pop()
            queue_right.popleft()

        queue_left.extend(queue_right)

        return queue_left

    queue = deque()

    for number in map(int, string):
        queue_new = add_parens(number)
        queue = fold_parens(queue, queue_new)

    return "".join(queue)


def parse_input(lines: Iterator[str]) -> Iterator[str]:
    number_of_tests = int(next(lines))
    for _ in range(number_of_tests):
        yield next(lines)


def main():
    case = 1
    for string in parse_input(sys.stdin):
        print("Case #%s: %s" % (case, solution(string.strip())))
        case += 1


if __name__ == "__main__":
    main()
