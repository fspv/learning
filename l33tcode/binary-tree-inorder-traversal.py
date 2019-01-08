class Solution:
    def inorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []

        result += self.inorderTraversal(root.left)
        result += [root.val]
        result += self.inorderTraversal(root.right)

        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        result = []
        node = root

        while True:
            while node is not None and node.left is not None:
                stack.append(node.left)
                node = node.left

            if not len(stack):
                break

            node = stack.pop()
            result.append(node.val)

            if node is not None and node.right is not None:
                node = node.right
                stack.append(node)
            else:
                node = None

        return result

# Tested in CLRS
