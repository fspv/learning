from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def compare(
            node_left_left: Optional[TreeNode],
            node_left_right: Optional[TreeNode],
            node_right_left: Optional[TreeNode],
            node_right_right: Optional[TreeNode],
        ) -> bool:
            node_left_left_val = node_left_left.val if node_left_left else -1
            node_left_right_val = node_left_right.val if node_left_right else -1
            node_right_left_val = node_right_left.val if node_right_left else -1
            node_right_right_val = node_right_right.val if node_right_right else -1

            return (node_left_left_val, node_left_right_val) == (
                node_right_left_val,
                node_right_right_val,
            )

        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True

            if not (left and right) or left.val != right.val:
                return False

            if compare(left.left, left.right, right.left, right.right):
                return dfs(left.left, right.left) and dfs(right.right, left.right)
            elif compare(left.right, left.left, right.left, right.right):
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            else:
                return False

        return dfs(root1, root2)
