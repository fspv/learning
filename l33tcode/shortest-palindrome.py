from typing import Tuple, List


class RollingHash:
    def __init__(self, string: str) -> None:
        self._hash = 0
        self._chars = 0
        self._alphabet_size = 26
        self._mod = 100

        for char in string:
            self.append(char)

    @staticmethod
    def _char_to_int(char: str) -> int:
        return ord(char) - ord("a") + 1

    def append(self, char: str) -> None:
        self._chars += 1
        self._hash = (
            int(self._hash * self._alphabet_size + self._char_to_int(char)) % self._mod
        )

    def appendleft(self, char: str) -> None:
        self._hash = (
            int(
                self._hash
                + self._char_to_int(char) * (self._alphabet_size ** self._chars)
            )
            % self._mod
        )
        self._chars += 1

    def popleft(self, char: str) -> None:
        self._chars -= 1
        self._hash -= (
            int((self._alphabet_size ** self._chars) * self._char_to_int(char))
            % self._mod
        )

    def __hash__(self) -> int:
        return self._hash

    def __repr__(self) -> str:
        return str(self._hash)


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


def longest_palindrome_from_beginning(target: str) -> int:
    hash_left_right = RollingHash("")
    hash_right_left = RollingHash("")
    longest_palindrome = 0

    for pos in range(len(target)):
        hash_left_right.append(target[pos])
        hash_right_left.appendleft(target[pos])

        if hash(hash_left_right) == hash(hash_right_left):
            if list(target[: pos + 1]) == list(reversed(target[: pos + 1])):
                longest_palindrome = pos + 1

    return longest_palindrome


def shortest_palindrome_rabin_karp(target: str) -> str:
    reversed_target = "".join(list(reversed(list(target))))

    length = longest_palindrome_from_beginning(target)
    offset = len(target) - length
    return reversed_target + (target[-offset:] if offset > 0 else "")


class Solution:
    def shortestPalindrome(self, target: str) -> str:
        return shortest_palindrome(target)
        # return shortest_palindrome_rabin_karp(target)
