from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple


# Definition for a binary tree node.
@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode]
    right: Optional[TreeNode]


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> Tuple[float, int, int]:  # (total, count, res)
            total, count, res = node.val, 1, 0

            for next_node in (node.left, node.right):
                if next_node:
                    total_sub, count_sub, res_sub = dfs(next_node)
                    total += total_sub
                    count += count_sub
                    res += res_sub

            if node.val == total // count:
                res += 1

            return total, count, res

        return dfs(root)[2] if root else 0
