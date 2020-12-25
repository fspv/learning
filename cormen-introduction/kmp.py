from typing import List


def compute_prefix_function(pattern: str) -> List[int]:
    prefix_function = [0] * len(pattern)

    matched = 0
    for pos in range(1, len(pattern)):
        while matched != 0 and pattern[pos] != pattern[matched]:
            matched = prefix_function[matched - 1]

        if pattern[pos] == pattern[matched]:
            matched += 1

        prefix_function[pos] = matched

    return prefix_function


def kmp_match(string: str, pattern: str) -> int:
    prefix_function = compute_prefix_function(pattern)

    matched = 0

    for pos in range(len(string)):
        while matched != 0 and string[pos] != pattern[matched]:
            matched = prefix_function[matched - 1]

        if string[pos] == pattern[matched]:
            matched += 1

        if matched == len(pattern):
            return pos - matched + 1

    return -1


class TestKMP:
    def test_compute_prefix_function(self) -> None:
        assert compute_prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]
        assert compute_prefix_function("aabab") == [0, 1, 0, 1, 0]

    def test_kmp_match(self) -> None:
        assert kmp_match("aaababaabaababaab", "aabab") == 1
