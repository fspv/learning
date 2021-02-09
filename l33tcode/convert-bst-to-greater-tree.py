from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, greater_sum: int) -> int:
            sum_right, sum_left = 0, 0
            node_val = node.val

            if node.right:
                sum_right = dfs(node.right, greater_sum)

            if node.left:
                sum_left = dfs(node.left, sum_right + greater_sum + node.val)

            node.val += greater_sum + sum_right

            return sum_left + sum_right + node_val

        if not root:
            return None

        dfs(root, 0)

        return root
