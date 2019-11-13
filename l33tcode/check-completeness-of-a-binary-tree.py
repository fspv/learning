# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        stack = [root]

        missing = False

        while stack:
            old_stack = stack
            stack = []

            for node in old_stack:
                if node.left:
                    if missing:
                        return False
                    stack.append(node.left)
                else:
                    missing = True
                if node.right:
                    if missing:
                        return False
                    stack.append(node.right)
                else:
                    missing = True

        return True
