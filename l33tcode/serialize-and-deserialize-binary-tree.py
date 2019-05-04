from collections import OrderedDict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return

        result = OrderedDict()
        result[1] = root.val

        stack = [(1, root)]

        while stack:
            old_stack = stack
            stack = []

            for off, node in old_stack:
                if node.left:
                    stack.append((off * 2, node.left))
                    result[off * 2] = node.left.val
                if node.right:
                    stack.append((off * 2 + 1, node.right))
                    result[off * 2 + 1] = node.right.val

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        root = TreeNode(data[1])
        tree = {1: root}
        data.pop(1)

        for pos, val in data.items():
            node = TreeNode(val)
            tree[pos] = node
            parent_node = tree[pos // 2]
            if parent_node is not None:
                if pos % 2 == 0:
                    parent_node.left = node
                else:
                    parent_node.right = node

        return root


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
result = codec.deserialize(codec.serialize(root))
print(result.val)
print(result.left.val)
print(result.right.val)
print(result.right.left.val)
