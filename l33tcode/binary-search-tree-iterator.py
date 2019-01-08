# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = [root]
        self.node = root

    def next(self, subtree_node=None):
        node = self.node

        while node is not None and node.left is not None:
            self.stack.append(node.left)
            node = node.left

        node = self.stack.pop()
        tmp_node = node

        if node is not None and node.right is not None:
            node = node.right
            self.stack.append(node)
        else:
            node = None

        self.node = node
        return tmp_node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0 and self.root is not None


# TODO: add test cases
