from typing import Set, List, Tuple, Dict


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
        self._hash = int(
            self._hash * self._alphabet_size + self._char_to_int(char)
        ) % self._mod

    def popleft(self, char: str) -> None:
        self._chars -= 1
        self._hash -= int(
            (self._alphabet_size ** self._chars) * self._char_to_int(char)
        ) % self._mod

    def __hash__(self) -> int:
        return self._hash

    def __repr__(self) -> str:
        return str(self._hash)


def repeating_substring(string: str, length: int) -> bool:
    seen: Dict[int, List[Tuple[int, int]]] = {}

    rolling_hash = RollingHash(string[:length])

    for start in range(len(string) - length):
        end = start + length

        rolling_hash.popleft(string[start])
        rolling_hash.append(string[end])

        if hash(rolling_hash) in seen:
            for prev_start, prev_end in seen[hash(rolling_hash)]:
                if string[start:end] == string[prev_start:prev_end]:
                    return True

        seen.setdefault(hash(rolling_hash), [])
        seen[hash(rolling_hash)].append((start, end))

    return False


def bisect_repeating_substring(string: str) -> int:
    left, right = 0, len(string)

    while left < right:
        middle = left + (right - left) // 2

        if repeating_substring(string, middle):
            left = middle + 1
        else:
            right = middle

    return left


class Solution:
    def longestRepeatingSubstring(self, string: str) -> int:
        return bisect_repeating_substring(string)
