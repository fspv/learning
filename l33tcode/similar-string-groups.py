from typing import List, Optional, Dict, Set


class TrieNode:
    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.children: Dict[str, TrieNode] = {}
        self.words: Set[int] = set()
        self.end = False


class DisjointSet:
    def __init__(self, size: int) -> None:
        self._counts = [0] * size
        self._roots = list(range(size))
        self.count = size

    def union(self, root_left: int, root_right: int) -> None:
        root_less, root_more = list(
            sorted([root_left, root_right], key=lambda x: self._counts[x])
        )

        self._roots[root_less] = root_more
        self._counts[root_more] += self._counts[root_less]

        self.count -= 1

    def find(self, node: int) -> int:
        if self._roots[node] != node:
            self._roots[node] = self.find(self._roots[node])

        return self._roots[node]


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(string_left: str, string_right: str) -> bool:
            if len(string_left) != len(string_right):
                return False

            different: List[int] = []

            for pos in range(len(string_left)):
                if string_left[pos] != string_right[pos]:
                    different.append(pos)

            if not different:
                return True

            if len(different) != 2:
                return False

            left_pos, right_pos = different

            return (string_left[left_pos], string_left[right_pos]) == (
                string_right[right_pos],
                string_right[left_pos],
            )

        def build_trie() -> TrieNode:
            root = TrieNode("")

            def add_word(word_pos: int, pos: int, node: TrieNode) -> None:
                word = strs[word_pos]

                if pos == len(word):
                    node.words.add(word_pos)
                    node.end = True
                    return

                node.children.setdefault(word[pos], TrieNode(word[pos]))
                add_word(word_pos, pos + 1, node.children[word[pos]])

                node.children.setdefault("*", TrieNode(word[pos]))
                add_word(word_pos, pos + 1, node.children["*"])

            for word_pos in range(len(strs)):
                add_word(word_pos, 0, root)

            return root

        def find_similar(
            word: str, pos: int, node: TrieNode, left: int, similar: Set[int]
        ) -> None:
            # Populate similar with similar values
            if node.end:
                if left in {0, 2}:
                    similar |= node.words

                return

            if left < 0:
                return

            find_similar(word, pos + 1, node.children[word[pos]], left, similar)
            find_similar(word, pos + 1, node.children["*"], left - 1, similar)

        disjoint_set = DisjointSet(len(strs))

        for left_pos in range(len(strs)):
            for right_pos in range(left_pos + 1, len(strs)):
                if is_similar(strs[left_pos], strs[right_pos]):
                    root_left, root_right = (
                        disjoint_set.find(left_pos),
                        disjoint_set.find(right_pos),
                    )

                    if root_left != root_right:
                        disjoint_set.union(root_left, root_right)

        # trie_root = build_trie()

        # for left_pos in range(len(strs)):
        #     similar: Set[int] = set()
        #     find_similar(strs[left_pos], 0, trie_root, 2, similar)

        #     for right_pos in similar:
        #         root_left, root_right = (
        #             disjoint_set.find(left_pos),
        #             disjoint_set.find(right_pos),
        #         )

        #         if root_left != root_right:
        #             disjoint_set.union(root_left, root_right)

        return disjoint_set.count
