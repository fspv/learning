from collections import defaultdict
from typing import DefaultDict, List


def compute_transition_function(pattern: str) -> List[DefaultDict[str, int]]:
    transition_function: List[DefaultDict[str, int]] = [
        defaultdict(int) for _ in range(len(pattern) + 1)
    ]

    alphabet = frozenset(pattern)

    for pos in range(len(pattern) + 1):
        for letter in alphabet:
            for offset in reversed(range(pos + 1)):
                if pattern[: offset + 1] == pattern[(pos - offset) : pos] + letter:
                    transition_function[pos][letter] = offset + 1
                    break
                else:
                    # Just to simplify testing, not strictly required
                    transition_function[pos][letter] = 0

    return transition_function


def match(target: str, pattern: str) -> int:
    transition_function: List[DefaultDict[str, int]] = compute_transition_function(
        pattern
    )

    init_state = 0

    state = init_state
    for pos in range(len(target)):
        state = transition_function[state][target[pos]]

        if state == len(target) - 1:
            return pos

    return -1


class TestMatch:
    def test_compute_transition_function(self) -> None:
        assert compute_transition_function("ababaca") == [
            {"a": 1, "b": 0, "c": 0},
            {"a": 1, "b": 2, "c": 0},
            {"a": 3, "b": 0, "c": 0},
            {"a": 1, "b": 4, "c": 0},
            {"a": 5, "b": 0, "c": 0},
            {"a": 1, "b": 4, "c": 6},
            {"a": 7, "b": 0, "c": 0},
            {"a": 1, "b": 2, "c": 0},
        ]

        assert compute_transition_function("aabab") == [
            {"a": 1, "b": 0},
            {"a": 2, "b": 0},
            {"a": 2, "b": 3},
            {"a": 4, "b": 0},
            {"a": 2, "b": 5},
            {"a": 1, "b": 0},
        ]

    def test_match(self) -> None:
        assert match("aaababaabaababaab", "aabab")
