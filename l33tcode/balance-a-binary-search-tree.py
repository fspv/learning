# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        def dfs1(node, stack):
            if node.left:
                dfs1(node.left, stack)

            stack.append(node)

            if node.right:
                dfs1(node.right, stack)


        stack = []

        dfs1(root, stack)

        def dfs2(stack, left, right):
            if left > right:
                return

            middle = (left + right) // 2
            node = stack[middle]

            node.left = dfs2(stack, left, middle - 1)
            node.right = dfs2(stack, middle + 1, right)

            return node

        return dfs2(stack, 0, len(stack) - 1)
