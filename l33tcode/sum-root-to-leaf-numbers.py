# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prev: int) -> int:
            if not node:
                return 0

            current = prev * 10 + node.val

            if not (node.left or node.right):
                return current

            total = 0
            if node.left:
                total += dfs(node.left, current)
            if node.right:
                total += dfs(node.right, current)

            return total

        return dfs(root, 0)
