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

        # Assign placeholder to last_removed to pass first iteration
        last_removed = TreeNode(None)
        last_removed.right = TreeNode(None)

        while stack:
            node, node_val = stack[-1]

            if not node.left and not node.right and node_val == summ:
                return True

            # Check if
            # 1. This node has no left child
            # 2. Last removed node was the child of this node
            # 3. Last removed was the rightmost member of the left subtree of \
            #    this node
            if not node.left or (node.left == last_removed or last_removed.right == None):
                last_removed, last_removed_val = stack.pop()
                if node.right:
                    stack.append((node.right, node_val + node.right.val))
            else:
                stack.append((node.left, node_val + node.left.val))

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
