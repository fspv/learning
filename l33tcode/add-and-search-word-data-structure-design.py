from typing import Dict, Optional


class TrieNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.children: Dict[str, TrieNode] = {}
        self.end = False
        self.word: Optional[str] = None


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = TrieNode(None)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self._trie

        for letter in word:
            node.children.setdefault(letter, TrieNode(letter))
            node = node.children[letter]

        node.end = True
        node.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def backtrack(node: TrieNode, word: str, pos: int) -> bool:
            if pos == len(word):
                return node.end

            letters = node.children.keys() if word[pos] == "." else word[pos]

            for next_letter in letters:
                if next_letter in node.children:
                    if backtrack(node.children[next_letter], word, pos + 1):
                        return True

            return False

        return backtrack(self._trie, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
