from typing import List, Optional, Tuple, Dict, Iterator


class Trie:
    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.word: Optional[str] = None
        self.children: Dict[str, Trie] = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie(None)
        visited = [[False] * len(row) for row in board]

        def add_word(root: Trie, word: str) -> None:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = Trie(char)
                node = node.children[char]

            node.word = word

        for word in words:
            add_word(root, word)

        rows, cols = len(board), len(board[0]) if board else 0

        def neighbours(row, col) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and not visited[neigh_row][neigh_col]
                ):
                    yield neigh_row, neigh_col

        result = set()

        def dfs(row: int, col: int, node: Trie) -> None:
            visited[row][col] = True

            if board[row][col] in node.children:
                cur_node = node.children[board[row][col]]

                if cur_node.word:
                    result.add(cur_node.word)

                for neigh_row, neigh_col in neighbours(row, col):
                    dfs(neigh_row, neigh_col, cur_node)

            visited[row][col] = False

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return list(result)
