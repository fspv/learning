# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        if root is None:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            old_stack = stack
            stack = []

            for node, prev_min, prev_max in old_stack:
                if node.left:
                    if node.left.val >= node.val or node.left.val <= prev_min:
                        return False
                    stack.append((node.left, prev_min, node.val))
                if node.right:
                    if node.right.val <= node.val or node.right.val >= prev_max:
                        return False
                    stack.append((node.right, node.val, prev_max))

        return True
