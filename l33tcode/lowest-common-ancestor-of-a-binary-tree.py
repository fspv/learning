class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return

        stack = [root]
        path = None
        last_removed = TreeNode(None)

        while stack:
            node = stack[-1]

            if node in [p, q]:
                if path:
                    if node != path[-1]:
                        common_len = min(len(stack), len(path))
                        for pos in range(common_len):
                            if stack[pos] != path[pos]:
                                return stack[pos - 1]
                        return stack[common_len - 1]
                else:
                    path = stack.copy()

            if node.left is None or last_removed in [node.right, node.left]:
                if node.right and node.right != last_removed:
                    stack.append(node.right)
                else:
                    last_removed = stack.pop()
            else:
                stack.append(node.left)
