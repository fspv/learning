from itertools import chain, zip_longest


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from chain(dfs(node.left), dfs(node.right))

        return all(l == r for l, r in zip_longest(dfs(root1), dfs(root2)))
