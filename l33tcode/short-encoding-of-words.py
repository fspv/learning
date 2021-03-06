from __future__ import annotations
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class TrieNode:
    children: Dict[str, TrieNode]


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def add_trie(root: TrieNode, word: str) -> None:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode({})

                node = node.children[char]

        def dfs(node: TrieNode, depth: int) -> int:
            if not node.children:
                return depth

            result = 0
            for next_node in node.children.values():
                result += dfs(next_node, depth + 1)

            return result

        root = TrieNode({})

        for word in words:
            add_trie(root, "".join(reversed(word)))

        return dfs(root, 1)
