from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: TrieNode())
        self.word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """

        node = self.root

        for s in word:
            node = node.children[s]

        node.word = True


    def _search_prefix(self, prefix):
        node = self.root

        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else:
                return

        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        result = self._search_prefix(word)

        return result is not None and result.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search_prefix(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
