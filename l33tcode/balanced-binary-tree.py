# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced = True
        def dfs(node: TreeNode) -> int:
            nonlocal balanced

            height_left, height_right = 0, 0

            if node.left:
                height_left = dfs(node.left)

            if node.right:
                height_right = dfs(node.right)

            if abs(height_left - height_right) > 1:
                balanced = False

            return max(height_left, height_right) + 1

        if not root:
            return True

        dfs(root)

        return balanced
