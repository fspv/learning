from typing import List, Set, Deque, Tuple, Dict
from collections import deque


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.word = -1

    def __repr__(self) -> str:
        return f"TrieNode: [children: {self.children}, word: {self.word}]"


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, words: List[str]) -> int:
        def distance(words: List[str], left: int, right: int) -> int:
            diff = 0
            for pos in range(len(words[left])):
                if words[left][pos] != words[right][pos]:
                    diff += 1

            return diff

        def gen_adj_list(words: List[str]) -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in words]

            for left in range(len(words)):
                for right in range(len(words)):
                    if distance(words, left, right) == 1:
                        adj_list[left].append(right)

            return adj_list

        def build_trie(words: List[str]) -> TrieNode:
            trie_root = TrieNode()

            for word in range(len(words)):
                trie_node = trie_root

                for pos in range(len(words[word])):
                    trie_node.children.setdefault(words[word][pos], TrieNode())
                    trie_node = trie_node.children[words[word][pos]]

                trie_node.word = word

            return trie_root

        def diff_by_one(trie_root: TrieNode, word: str) -> List[int]:
            result = []

            def dfs(trie_node: TrieNode, pos: int, skip_pos: int) -> None:
                if pos == len(word):
                    result.append(trie_node.word)
                    return

                if pos == skip_pos:
                    for child in trie_node.children.keys():
                        dfs(trie_node.children[child], pos + 1, skip_pos)
                elif word[pos] in trie_node.children:
                    dfs(trie_node.children[word[pos]], pos + 1, skip_pos)

            for skip_pos in range(len(word)):
                dfs(trie_root, 0, skip_pos)

            return result

        if end_word not in words:
            return 0

        if begin_word not in words:
            words.append(begin_word)

        # adj_list: List[List[int]] = gen_adj_list(words)
        trie_root: TrieNode = build_trie(words)

        # print(trie_root)

        src, dst = words.index(begin_word), words.index(end_word)

        queue: Deque[Tuple[int, int]] = deque()

        queue.append((src, 1))

        visited: Set[int] = {src}

        while queue:
            word, length = queue.popleft()

            if word == dst:
                return length

            for next_word in diff_by_one(trie_root, words[word]):
                if next_word not in visited:
                    queue.append((next_word, length + 1))
                    visited.add(next_word)

        return 0
