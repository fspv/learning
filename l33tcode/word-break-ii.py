class TrieNode:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.word = None
        self.next = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = [None for _ in range(len(s))]

        def dfs_build_trie(word: str, pos: str, trie_prev: TrieNode) -> None:
            if pos == len(word):
                trie_prev.end = True
                trie_prev.word = word
                return

            trie_prev.next.setdefault(word[pos], TrieNode(word[pos]))

            dfs_build_trie(word, pos + 1, trie_prev.next[word[pos]])

        def build_trie(word_dict: List[str]):
            trie_root = TrieNode(None)
            for word in word_dict:
                dfs_build_trie(word, 0, trie_root)
            return trie_root

        def dfs(
            string: str, pos: int, trie_node: TrieNode, trie_root: TrieNode
        ) -> List[List[str]]:
            if pos == len(string) - 1:
                if trie_node.end and trie_node.val == string[pos]:
                    return [[trie_node.word]]
                else:
                    return []

            result = []

            next_pos = pos + 1

            if string[next_pos] in trie_node.next:
                for next_path in dfs(
                    string, next_pos, trie_node.next[string[next_pos]], trie_root
                ):
                    result.append(next_path)

            if trie_node.end and string[next_pos] in trie_root.next:
                if cache[pos] is not None:
                    for res in cache[pos]:
                        result.append(res.copy() + [trie_node.word])
                else:
                    tmp = []
                    for next_path in dfs(
                        string, next_pos, trie_root.next[string[next_pos]], trie_root
                    ):
                        tmp.append(next_path.copy())
                        next_path.append(trie_node.word)
                        result.append(next_path)
                    cache[pos] = tmp

            return result

        trie_root = build_trie(wordDict)
        sentences = dfs(s, -1, trie_root, trie_root)

        return [" ".join(reversed(sentence)) for sentence in sentences]
