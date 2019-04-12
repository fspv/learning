# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive one
    def maxDepth(self, node, depth=0):
        if node is None:
            return depth

        return max(
            self.maxDepth(node.left, depth + 1),
            self.maxDepth(node.right, depth + 1)
        )

    # Non-recursive one
    def maxDepth(self, root):
        stack = [root] if root else []
        level = 0

        while stack:
            level += 1
            old_stack = stack
            stack = []

            for node in old_stack:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return level
