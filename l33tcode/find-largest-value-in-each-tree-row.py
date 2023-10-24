from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    val: int
    left: Optional[None]
    right: Optional[None]


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        def dfs(node: TreeNode, level: int) -> None:
            if len(result) <= level:
                result.append(node.val)

            result[level] = max(result[level], node.val)

            if node.left:
                dfs(node.left, level + 1)

            if node.right:
                dfs(node.right, level + 1)

        if root:
            dfs(root, 0)

        return result
