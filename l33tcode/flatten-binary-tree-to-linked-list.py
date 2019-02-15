# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node is not None:
            # Try to insert right node into the rightmost position of the
            # left subtree
            if node.right is not None:
                if node.left is not None:
                    tmp_node = node.left
                    while tmp_node.right is not None:
                        tmp_node = tmp_node.right
                    tmp_node.right = node.right

                    # Reassign left subtree to the place of removed subtree
                    node.right = node.left
                    node.left = None
            else:
                # Move left subtree to the place of the empty right subtree
                if node.left is not None:
                    node.right = node.left
                    node.left = None

            node = node.right

# TODO: add tests here
# Test cases:
# [] -> []
# [0] -> [0]
# [1, 2, 5, 3, 4, None, 6] -> [1, None, 2, None, 3, None, 4, None, 5, None, 6]
