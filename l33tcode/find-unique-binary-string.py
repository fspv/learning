from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TrieNode:
    value: str
    children: dict[str, TrieNode]

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        trie = TrieNode("0", {})

        def add_trie(node: TrieNode, num: str) -> None:
            for pos in range(len(num)):
                if num[pos] in node.children:
                    node = node.children[num[pos]]
                else:
                    new_node = TrieNode(num[pos], {})
                    node.children[num[pos]] = new_node
                    node = new_node

        for num in nums:
            add_trie(trie, num)

        num_len = len(nums[0])

        stack: list[str] = []

        def dfs(pos: int, node: TrieNode) -> bool:
            if pos == num_len:
                return False

            if set(node.children) == {"0", "1"}:
                stack.append("0")
                if dfs(pos + 1, node.children["0"]):
                    return True
                stack.pop()
                stack.append("1")
                if dfs(pos + 1, node.children["1"]):
                    return True
                stack.pop()
            elif list(node.children) == ["0"]:
                stack.extend(["1"] * (num_len - pos))
                return True
            elif list(node.children) == ["1"]:
                stack.extend(["0"] * (num_len - pos))
                return True
            else:
                stack.extend(["0"] * (num_len - pos))
                return True

            return False

        dfs(0, trie)

        return "".join(stack)

