import logging
import random
import sys
from typing import Dict, List, Set, Tuple


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.end = False
        self.word = -1

    def __repr__(self) -> str:
        return f"TrieNode({list(self.children.keys())})"


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
    array: List[str],
) -> Tuple[List[List[bool]], List[List[bool]]]:
    result_lr: List[List[bool]] = []
    result_rl: List[List[bool]] = []

    for word in array:
        result_lr.append(
            list(
                map(
                    lambda x: any(x),
                    zip(manacher(list(word), 0), manacher(list(word), 1)),
                )
            )
        )
        result_rl.append(
            list(
                map(
                    lambda x: any(x),
                    zip(
                        manacher(list(reversed(word)), 0),
                        manacher(list(reversed(word)), 1),
                    ),
                )
            )
        )

    return result_lr, result_rl


def build_trie(strings: List[List[str]]) -> TrieNode:
    trie_root = TrieNode()

    for word_pos, word in enumerate(strings):
        trie_node = trie_root

        for pos in range(len(word)):
            trie_node.children.setdefault(word[pos], TrieNode())

            trie_node = trie_node.children[word[pos]]

        trie_node.end = True
        trie_node.word = word_pos

    return trie_root


def search_trie(
    word: List[str], is_palindrome_till_end: List[bool], trie_root: TrieNode
) -> List[int]:
    trie_node = trie_root
    result: List[int] = []

    if trie_node.end and is_palindrome_till_end[0]:
        result.append(trie_node.word)

    for pos in range(len(word)):
        if word[pos] in trie_node.children:
            trie_node = trie_node.children[word[pos]]
        else:
            break

        if is_palindrome_till_end[pos + 1] and trie_node.end:
            result.append(trie_node.word)

    return result


def palindrome_concatenation(strings: List[str]) -> List[Tuple[int, int]]:
    strings_regular = list(map(lambda x: list(x), strings))
    strings_reversed = list(map(lambda x: list(reversed(x)), strings))
    trie_root = build_trie(strings_regular)
    trie_root_reversed = build_trie(strings_reversed)
    result_lr, result_rl = palindromes_till_the_end(strings)

    palindrome_pairs: Set[Tuple[int, int]] = set()

    for word_pos in range(len(strings)):
        palindrome_with = search_trie(
            strings_regular[word_pos], result_lr[word_pos], trie_root_reversed
        )
        palindrome_pairs |= set(
            map(
                lambda x: (x[0], x[1]),
                zip([word_pos] * len(palindrome_with), palindrome_with),
            )
        )

        palindrome_with = search_trie(
            strings_reversed[word_pos], result_rl[word_pos], trie_root
        )
        palindrome_pairs |= set(
            map(
                lambda x: (x[0], x[1]),
                zip(palindrome_with, [word_pos] * len(palindrome_with)),
            )
        )

    return list(
        sorted(
            filter(
                lambda x: x[0] != x[1],
                map(lambda x: (x[0] + 1, x[1] + 1), palindrome_pairs),
            )
        )
    )


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
