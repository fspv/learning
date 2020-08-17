from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        nodes_below = [0] * n
        nodes = [None] * n

        def dfs_augment(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            nodes_below_left = dfs_augment(node.left)
            nodes_below_right = dfs_augment(node.right)

            nodes_below[node.val - 1] = nodes_below_left + nodes_below_right + 1
            nodes[node.val - 1] = nodes[node.val - 1] or node

            return nodes_below[node.val - 1]

        nodes_total = dfs_augment(root)

        if nodes_total - nodes_below[x - 1] > nodes_below[x - 1]:
            return True

        for node in [nodes[x - 1].left, nodes[x - 1].right]:
            if node and nodes_total - nodes_below[node.val - 1] < nodes_below[node.val - 1]:
                return True

        return False
