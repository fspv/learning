# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSumDFS(self, root, summ):
        if root is None:
            return False

        stack = [(root, root.val)]
        last_removed = None

        while stack:
            node, node_val = stack[-1]

            if not node.left and not node.right and node_val == summ:
                return True

            if last_removed and node.left == last_removed:
                if node.right:
                    last_removed, last_removed_val = stack.pop()
                    stack.append((node.right, node_val + node.right.val))
                else:
                    last_removed, last_removed_val = stack.pop()
            elif last_removed and last_removed.right == None:
                last_removed, last_removed_val = stack.pop()
                if node.right:
                    stack.append((node.right, node_val + node.right.val))
            else:
                if node.left:
                    stack.append((node.left, node_val + node.left.val))
                elif node.right:
                    last_removed, last_removed_val = stack.pop()
                    stack.append((node.right, node_val + node.right.val))
                else:
                    last_removed, last_removed_val = stack.pop()

        return False

    def hasPathSumBFS(self, root, summ):
        if root is None:
            return False

        stack = [(root, root.val)]

        while stack:
            old_stack = stack
            stack = []

            for node, node_val in old_stack:
                if node.left or node.right:
                    if node.left:
                        stack.append((node.left, node_val + node.left.val))
                    if node.right:
                        stack.append((node.right, node_val + node.right.val))
                else:
                    if node_val == summ:
                        return True

        return False
