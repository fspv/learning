# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        left = lambda x: x * 2 + 1
        right = lambda x: x * 2 + 2

        result = 0

        if not root:
            return result

        stack = [(root, 0)]

        while stack:
            result = max(stack[-1][1] - stack[0][1] + 1, result)

            old_stack = stack
            stack = []

            for node, pos in old_stack:
                if node.left:
                    stack.append((node.left, left(pos)))
                if node.right:
                    stack.append((node.right, right(pos)))

        return result

