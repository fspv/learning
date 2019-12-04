# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        def dfs(node):
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)

            if node.val < L:
                return node.right
            elif node.val > R:
                return node.left
            else:
                return node

        return dfs(root)
