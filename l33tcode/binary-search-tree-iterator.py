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


class BSTIterator2:
    def __init__(self, root: TreeNode):
        self._node = root
        self._left_traversed = False

    @staticmethod
    def _is_rightmost(node: TreeNode) -> bool:
        right = node.right

        if right and right.left:
            return right.left.val < node.val

        return False

    @staticmethod
    def _set_link(node: TreeNode) -> None:
        left = node.left

        while left.right:
            left = left.right

        left.right = node

    def next(self) -> int:
        while not self._left_traversed and self._node.left:
            self._set_link(self._node)
            self._node = self._node.left

        result = self._node

        if self._is_rightmost(self._node):
            tmp = self._node

            self._node = self._node.right
            self._left_traversed = True

            tmp.right = None
        else:
            self._node = self._node.right
            self._left_traversed = False

        return result.val

    def hasNext(self) -> bool:
        return bool(self._node)


# TODO: add test cases
