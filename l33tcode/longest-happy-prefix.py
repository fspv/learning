from typing import List


class RollingHash:
    def __init__(self, string: str) -> None:
        self._hash = 0
        self._pow = 1
        self._alphabet_size = 26
        self._mod = 2 ** 63

        for char in string:
            self.append(char)

    @staticmethod
    def _char_to_int(char: str) -> int:
        return ord(char) - ord("a") + 1

    def append(self, char: str) -> None:
        self._pow *= self._alphabet_size
        self._hash = (
            int(self._hash * self._alphabet_size + self._char_to_int(char)) % self._mod
        )

    def appendleft(self, char: str) -> None:
        self._hash = int(self._hash + self._char_to_int(char) * self._pow) % self._mod
        self._pow *= self._alphabet_size

    def popleft(self, char: str) -> None:
        self._pow //= self._alphabet_size
        self._hash -= int(self._pow * self._char_to_int(char)) % self._mod

    def __hash__(self) -> int:
        return self._hash

    def __repr__(self) -> str:
        return str(self._hash)


def compute_prefix_function(pattern: str) -> List[int]:
    prefix_function = [0] * len(pattern)

    matched = 0
    for pos in range(1, len(pattern)):
        while matched != 0 and pattern[matched] != pattern[pos]:
            matched = prefix_function[matched - 1]

        if pattern[matched] == pattern[pos]:
            matched += 1

        prefix_function[pos] = matched

    return prefix_function


class Solution:
    def longestPrefix(self, string: str) -> str:
        return string[: compute_prefix_function(string)[-1]]

    def longestPrefixRabinKarp(self, string: str) -> str:
        hash_left_right = RollingHash("")
        hash_right_left = RollingHash("")

        longest_prefix = ""

        for pos in range(len(string) - 1):
            hash_left_right.append(string[pos])
            hash_right_left.appendleft(string[-pos - 1])

            if hash(hash_left_right) == hash(hash_right_left):
                if string[: pos + 1] == string[-pos - 1 :]:
                    longest_prefix = string[: pos + 1]

        return longest_prefix
