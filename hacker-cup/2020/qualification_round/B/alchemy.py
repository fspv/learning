#!/usr/bin/env python3
from __future__ import annotations

import sys
from typing import List, Iterator


def build_stone(shards: List[str]) -> List[str]:
    stack = []

    for color in shards:
        stack.append(color)

        while len(stack) >= 3 and len(set(stack[-3:])) == 2:
            colors = [stack.pop(), stack.pop(), stack.pop()]
            new_color = "A" if colors.count("A") > 1 else "B"

            stack.append(new_color)

    return stack


def read_number_of_stones(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_number_shards(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_shard_list(lines: Iterator[str]) -> List[str]:
    shards_number = read_number_shards(lines)
    shards = list(next(lines).rstrip())

    if len(shards) > shards_number:
        raise RuntimeError(
            f"Shards length {len(shards)} is different"
            f"from what is expected {shards_number}"
        )

    return shards


def read_stones(lines: Iterator[str]) -> Iterator[List[str]]:
    for _ in range(read_number_of_stones(lines)):
        yield read_shard_list(lines)


def print_answer(case: int, answer: bool) -> None:
    result = "Y" if answer else "N"

    print(f"Case #{case}: {result}")


def main() -> None:
    case = 1

    for shards in read_stones(sys.stdin):
        stack = build_stone(shards)
        answer = len(stack) == 1
        print_answer(case, answer)
        case += 1


if __name__ == "__main__":
    main()
