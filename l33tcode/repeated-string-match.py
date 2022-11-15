from typing import List, Tuple


class RollingHash:
    def __init__(self, string: str) -> None:
        self._hash = 0
        self._chars = 0
        self._alphabet_size = 26

        for char in string:
            self.append(char)

    @staticmethod
    def _char_to_int(char: str) -> int:
        return ord(char) - ord("a") + 1

    def append(self, char: str) -> None:
        self._chars += 1
        self._hash = self._hash * self._alphabet_size + self._char_to_int(char)

    def popleft(self) -> None:
        self._chars -= 1
        self._hash %= self._alphabet_size ** self._chars

    def __eq__(self, other: object) -> bool:
        return isinstance(other, RollingHash) and self._hash == other._hash


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        a_hash = RollingHash("".join([a[pos % len(a)] for pos in range(len(b))]))
        b_hash = RollingHash(b)

        right = len(b)

        for left in range(len(a)):
            if a_hash == b_hash:
                if "".join([a[pos % len(a)] for pos in range(left, right)]) == b:
                    return right // len(a) + int(right % len(a) > 0)

            a_hash.append(a[right % len(a)])
            a_hash.popleft()

            right += 1

        return -1

    def repeatedStringMatchBruteForce(self, a: str, b: str) -> int:
        def try_match(pos: int) -> Tuple[bool, int]:
            a_ptr, b_ptr = pos, 0
            repeats = 1

            while a[a_ptr] == b[b_ptr]:
                b_ptr += 1

                if b_ptr == len(b):
                    return True, repeats

                a_ptr = (a_ptr + 1) % len(a)

                if a_ptr == 0:
                    repeats += 1

            return False, 0

        for pos in range(len(a)):
            ok, repeats = try_match(pos)

            if ok:
                return repeats

        return -1
