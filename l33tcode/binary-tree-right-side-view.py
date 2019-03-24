# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        result = []

        if not root:
            return result

        stack = [root]

        while stack:
            old_stack = stack
            stack = []

            result.append(old_stack[-1].val)

            for node in old_stack:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return result
