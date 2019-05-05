# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(node, added):
            if node is None:
                return added
            node.val += inorder(node.right, added)
            return inorder(node.left, node.val)

        if root:
            inorder(root, 0)
            return root
        else:
            return
