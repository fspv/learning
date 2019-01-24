class Solution:
    def traverse_tree_rec(self, root):
        result = []
        if root.left is not None:
            result += self.traverse_tree(root.left)
        result.append(root)
        if root.right is not None:
            result += self.traverse_tree(root.right)
        return result

    def traverse_tree(self, root, k):
        stack = [root]
        node = None
        count = 0

        while len(stack):
            if stack[-1].left is not None and \
               stack[-1].left is not node and \
               (node is None or node.right is not None):
                stack.append(stack[-1].left)
            else:
                node = stack.pop()
                count += 1
                if count == k:
                    return node
                if node.right is not None:
                    stack.append(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.traverse_tree(root, k).val
