# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [root]
        count = 0
        while stack:
            old_stack = stack
            stack = []

            for node in old_stack:
                count += 1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return count
