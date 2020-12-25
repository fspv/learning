from typing import Tuple, List


def compute_prefix_function(pattern: str) -> List[int]:
    prefix_function = [0] * len(pattern)

    matched = 0
    for prefix in range(1, len(pattern)):
        while matched != 0 and pattern[prefix] != pattern[matched]:
            matched = prefix_function[matched - 1]

        if pattern[prefix] == pattern[matched]:
            matched += 1

        prefix_function[prefix] = matched

    return prefix_function


def longest_match(target: str, pattern: str) -> int:
    prefix_function = compute_prefix_function(pattern)

    matched = 0
    for pos in range(len(target)):
        while matched != 0 and target[pos] != pattern[matched]:
            matched = prefix_function[matched - 1]

        if target[pos] == pattern[matched]:
            matched += 1

    return matched


def shortest_palindrome(target: str) -> str:
    reversed_target = "".join(list(reversed(list(target))))

    length = longest_match(reversed_target, target)
    offset = len(target) - length
    return reversed_target + (target[-offset:] if offset > 0 else "")


class Solution:
    def shortestPalindrome(self, target: str) -> str:
        return shortest_palindrome(target)
