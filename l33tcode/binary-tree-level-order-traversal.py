# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        stacked_stack = [[root]]
        result = []

        while stacked_stack[-1]:
            stacked_stack.append([])
            result.append([])
            for node in stacked_stack[-2]:
                result[-1].append(node.val)
                if node.left:
                    stacked_stack[-1].append(node.left)
                if node.right:
                    stacked_stack[-1].append(node.right)

        return result
