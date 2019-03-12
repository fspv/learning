# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bst(self, root, search):
        stack = [root]

        while True:
            node = stack[-1]

            if node == search:
                return stack

            stack.append(node.right if node.val < search.val else node.left)

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        p_stack = self.bst(root, p)
        q_stack = self.bst(root, q)

        common_len = min(len(p_stack), len(q_stack))

        for pos in range(common_len):
            if p_stack[pos] != q_stack[pos]:
                return q_stack[pos - 1]

        return q_stack[common_len - 1]
