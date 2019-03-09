# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return

        node = TreeNode(val)
        current_node = root

        while True:
            if node.val < current_node.val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    break

        return root
