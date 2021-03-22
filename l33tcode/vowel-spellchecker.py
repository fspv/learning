from __future__ import annotations

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class TrieNode:
    end: bool
    word: str
    value: str
    children: Dict[str, TrieNode]


def add_word(root: TrieNode, word: str) -> None:
    vowels = {"a", "e", "i", "o", "u"}

    node = root

    for char in map(lambda c: c.lower(), word):
        char = "*" if char in vowels else char

        node.children.setdefault(char, TrieNode(False, "", char, {}))
        node = node.children[char]

    if not node.end:
        node.end = True
        node.word = word


def search_word(root: TrieNode, word: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    result = ""

    def dfs(node: TrieNode, pos: int) -> None:
        nonlocal result

        if pos == len(word):
            if node.end:
                result = node.word

            return

        char = "*" if word[pos] in vowels else word[pos].lower()
        if char in node.children:
            dfs(node.children[char], pos + 1)

    dfs(root, 0)

    return result


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        root = TrieNode(False, "", "", {})
        word_set = set(wordlist)
        word_map: Dict[str, str] = {}
        for word in wordlist:
            word_map.setdefault(word.lower(), word)

        for word in wordlist:
            add_word(root, word)

        result: List[str] = []

        for query in queries:
            if query in word_set:
                result.append(query)
                continue

            if query.lower() in word_map:
                result.append(word_map[query.lower()])
                continue

            word = search_word(root, query.lower())

            result.append(word)

        return result
