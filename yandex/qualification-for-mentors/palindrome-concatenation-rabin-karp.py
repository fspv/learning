import logging
import random
import sys
from collections import defaultdict
from typing import DefaultDict, List, Tuple

ALPHABET_SIZE = 26


class RollingHash:
    def __init__(self, word: str) -> None:
        self.hash = 0
        self._alphabet_size = ALPHABET_SIZE

        for char in word:
            self.add(char)

    def add(self, char: str) -> None:
        self.hash *= self._alphabet_size
        self.hash += ord("z") - ord(char)

    def __eq__(self, other: object) -> bool:
        return self.hash == other.hash


def manacher(array: List[str], left_offset: int) -> List[bool]:
    left, right = 0, -1
    cache = [0] * len(array)
    result = [False] * (len(array) + 1)
    result[-1] = True

    for pos in range(len(array)):
        radius = (
            1 - left_offset
            if pos > right
            else min(cache[left + right - (pos - left_offset)] + 1, right - pos + 1)
        )

        while (
            0 <= pos - left_offset - radius
            and pos + radius < len(array)
            and array[pos - left_offset - radius] == array[pos + radius]
        ):
            radius += 1

        radius -= 1

        cache[pos] = radius

        if pos + radius == len(array) - 1:
            result[pos - left_offset - radius] = True

        if pos + radius > right:
            left = pos - left_offset - radius
            right = pos + radius

    return result


def palindromes_till_the_end(
    strings: List[str],
) -> Tuple[List[List[bool]], List[List[bool]]]:
    is_palindrome_forward: List[List[bool]] = []
    is_palindrome_back: List[List[bool]] = []

    for string in strings:
        is_palindrome_forward.append(
            list(
                map(
                    lambda x: any(x),
                    zip(manacher(list(string), 0), manacher(list(string), 1)),
                )
            )
        )
        is_palindrome_back.append(
            list(
                map(
                    lambda x: any(x),
                    zip(
                        manacher(list(reversed(string)), 0),
                        manacher(list(reversed(string)), 1),
                    ),
                )
            )
        )

    return is_palindrome_forward, is_palindrome_back


def palindrome_concatenation(strings: List[str]) -> List[Tuple[int, int]]:
    is_palindrome_forward, is_palindrome_back = palindromes_till_the_end(strings)

    string_hash_map_forward: DefaultDict[int, List[int]] = defaultdict(list)
    string_hash_map_back: DefaultDict[int, List[int]] = defaultdict(list)

    # Populate hash maps, which later will be used for search
    for strings_pos in range(len(strings)):
        rolling_hash = RollingHash("".join(reversed(strings[strings_pos])))
        string_hash_map_back[rolling_hash.hash].append(strings_pos)

    for strings_pos in range(len(strings)):
        rolling_hash = RollingHash(strings[strings_pos])
        string_hash_map_forward[rolling_hash.hash].append(strings_pos)

    result: List[Tuple[int, int]] = []

    for strings_pos in range(len(strings)):
        # Search forward substing in backward map
        rolling_hash = RollingHash("")

        for string_pos in range(len(strings[strings_pos])):
            rolling_hash.add(strings[strings_pos][string_pos])

            for index in string_hash_map_back[rolling_hash.hash]:
                # Filter out same strings
                if index == strings_pos:
                    continue

                # Check for hash collisions
                if strings[strings_pos][: string_pos + 1] != "".join(
                    reversed(strings[index])
                ):
                    continue

                if is_palindrome_forward[strings_pos][string_pos + 1]:
                    result.append((strings_pos + 1, index + 1))

        # Search backward substring in forward map
        rolling_hash = RollingHash("")

        for string_pos in reversed(range(len(strings[strings_pos]))):
            rolling_hash.add(strings[strings_pos][string_pos])

            for index in string_hash_map_forward[rolling_hash.hash]:
                # Filter out same strings
                if index == strings_pos:
                    continue

                # Check for hash collisions
                if strings[strings_pos][string_pos:] != "".join(
                    reversed(strings[index])
                ):
                    continue

                if is_palindrome_back[strings_pos][
                    len(strings[strings_pos]) - string_pos
                ]:
                    result.append((index + 1, strings_pos + 1))

    x = list(sorted(set(result)))

    return x


def get_number_of_strings() -> int:
    line = sys.stdin.readline()

    try:
        number_of_strings = int(line)
    except ValueError:
        logging.exception(f"Can't parse: {line}")

    return number_of_strings


def get_string() -> str:
    return sys.stdin.readline().rstrip()


def main() -> None:
    strings: List[str] = []
    for _ in range(get_number_of_strings()):
        strings.append(get_string())

    for left, right in palindrome_concatenation(strings):
        print(f"{left} {right}")


if __name__ == "__main__":
    main()


class TestPalindromeConcatenation:
    def test_case1(self) -> None:
        assert palindrome_concatenation(["a", "abbaa", "bba", "abb"]) == [
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 4),
            (4, 1),
            (4, 3),
        ]

    def test_case2(self) -> None:
        assert palindrome_concatenation(["pa", "lap", "palk", "pal"]) == [
            (1, 2),
            (2, 4),
            (3, 2),
            (4, 2),
        ]

    def test_case3(self) -> None:
        assert palindrome_concatenation(["aba", "abba"]) == []

    def test_large1(self) -> None:
        letters = list("abcdefghijklmnopqrstuvwxyz")
        strings = [
            "".join(random.choices(letters, k=random.randint(1, 30)))
            for _ in range(100000)
        ]

        palindrome_concatenation(strings)
