# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        stack = [root]

        while stack:
            node = stack.pop()

            if not node:
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            node.left, node.right = node.right, node.left

        return root


    def invertTreeRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node:
                node.left, node.right = dfs(node.right), dfs(node.left)
            return node

        return dfs(root)
