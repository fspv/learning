from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode) -> Tuple[TreeNode, TreeNode]:
            left_left, left_right, right_left, right_right = node, node, node, node

            if node.left:
                left_left, left_right = dfs(node.left)
                if left_right:
                    left_right.right = node

            if node.right:
                right_left, right_right = dfs(node.right)
                node.right = right_left

            node.left = None

            return left_left, right_right

        left, right = dfs(root)

        return left
