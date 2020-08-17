from typing import List, Dict, Optional


class TrieNode:
    def __init__(self, value: Optional[str]) -> None:
        self.value = value
        self.children: Dict[str, TrieNode] = {}

        self.end = False
        self.word: Optional[str] = None  # not necessary in this task


def build_trie(words: List[str]) -> TrieNode:
    trie_root = TrieNode(None)

    for word in words:
        trie_node = trie_root

        for char in word:
            trie_node.children.setdefault(char, TrieNode(char))
            trie_node = trie_node.children[char]

        trie_node.end = True
        trie_node.word = word

    return trie_root


class StreamChecker:
    def __init__(self, words: List[str]) -> None:
        self._trie = build_trie(words)
        self._trie_ptrs = [self._trie]

    def query(self, letter: str) -> bool:
        trie_ptrs_new = [self._trie]

        result = False

        for trie_node in self._trie_ptrs:
            if letter in trie_node.children:
                result = result or trie_node.children[letter].end
                trie_ptrs_new.append(trie_node.children[letter])

        self._trie_ptrs = trie_ptrs_new

        return result


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
