from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> Optional[TreeNode]:
        result: Optional[TreeNode] = None

        def dfs(node_original: TreeNode, node_cloned: TreeNode) -> None:
            nonlocal result

            if node_original == target:
                result = node_cloned

            if node_original.left:
                dfs(node_original.left, node_cloned.left)

            if node_original.right:
                dfs(node_original.right, node_cloned.right)

        dfs(original, cloned)

        return result
