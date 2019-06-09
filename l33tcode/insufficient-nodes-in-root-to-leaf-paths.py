class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root is None:
            return root

        def dfs(node, sum_before):
            if node is None:
                return sum_before < limit

            left = dfs(node.left, node.val + sum_before)

            right = dfs(node.right, node.val + sum_before)

            if left:
                node.left = None

            if right:
                node.right = None

            return left and right

        delete = dfs(root, 0)

        return None if delete else root
