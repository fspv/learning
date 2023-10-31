from __future__ import annotations

from dataclasses import dataclass
from typing import Counter, Optional, List


# Definition for a binary tree node.
@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode]
    right: Optional[TreeNode]


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter: Counter[int] = Counter()

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            counter[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        max_freq = max(counter.values()) if counter else -1

        return [val for val, freq in counter.items() if freq == max_freq]
