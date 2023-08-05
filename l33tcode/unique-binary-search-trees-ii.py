from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    # Definition for a binary tree node.
    @dataclass
    class TreeNode:
        val: int
        left: Optional[TreeNode] = None
        right: Optional[TreeNode] = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(start: int, stop: int) -> List[TreeNode]:
            subtrees: List[TreeNode] = []

            for split in range(start, stop):
                for left in dfs(start, split) or [None]:
                    for right in dfs(split + 1, stop) or [None]:
                        node = TreeNode(split)
                        node.left, node.right = left, right

                        subtrees.append(node)

            return subtrees

        return dfs(1, n + 1)
