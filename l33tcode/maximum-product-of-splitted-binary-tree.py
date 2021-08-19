from typing import Tuple

MOD = 10 ** 9 + 7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, total_sum: int) -> Tuple[int, int]:
            if not node:
                return 0, 0

            sum_left, max_prod_left = dfs(node.left, total_sum)
            sum_right, max_prod_right = dfs(node.right, total_sum)

            sum_subtree = sum_left + sum_right + node.val
            prod = (total_sum - sum_subtree) * sum_subtree

            return (sum_subtree, max(prod, max_prod_left, max_prod_right))

        total_sum = dfs(root, 0)[0]

        return dfs(root, total_sum)[1] % MOD
