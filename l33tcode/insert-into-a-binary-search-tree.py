# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        node = root
        parent = None

        while node:
            parent = node
            if node.val < new_node.val:
                node = node.right
            else:
                node = node.left

        if not parent:
            root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        elif new_node.val > parent.val:
            parent.right = new_node
        else:
            pass

        return root

    def insertIntoBST1(self, root, val):
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
