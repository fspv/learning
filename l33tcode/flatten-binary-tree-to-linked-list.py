# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insert_subtree_into_subtree(self, subtree, target_subtree):
        if target_subtree is None:
            return

        if target_subtree.left is not None and target_subtree.right is None:
            target_subtree.left, target_subtree.right = target_subtree.right, target_subtree.left

            self.insert_subtree_into_subtree(target_subtree.left, target_subtree.right)

        if target_subtree.left is not None and target_subtree.right is not None:
            if target_subtree.left.val < target_subtree.right.val:
                target_subtree.left, target_subtree.right = target_subtree.right, target_subtree.left

            self.insert_subtree_into_subtree(target_subtree.left, target_subtree.right)
            target_subtree.left = None

        if subtree is None:
            self.insert_subtree_into_subtree(subtree, target_subtree.right)
        elif target_subtree.right is None:
            target_subtree.right = subtree
        else:
            node = target_subtree.right
            while node is not None:
                if node.right is None:
                    node.right = subtree
                    break

                if subtree.val <= node.right.val:
                    self.insert_subtree_into_subtree(node.right, subtree)
                    node.right = subtree
                    break

                node = node.right


    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.insert_subtree_into_subtree(None, root)

# TODO: not working on some cases
