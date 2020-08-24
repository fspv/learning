# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def is_leaf(node: TreeNode) -> bool:
            if not node:
                return False

            if not node.left and not node.right:
                return True

            return False

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            result = 0

            if is_leaf(node.left):
                result += node.left.val

            result += dfs(node.left)
            result += dfs(node.right)

            return result

        return dfs(root)
