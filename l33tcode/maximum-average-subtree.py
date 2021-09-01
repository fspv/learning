from typgin import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_average = 0

        def dfs(node: TreeNode) -> Tuple[int, int]:  # number of elements, subtree sum
            nonlocal max_average
            elements_left, sum_left = 0, 0
            elements_right, sum_right = 0, 0

            if node.left:
                elements_left, sum_left = dfs(node.left)

            if node.right:
                elements_right, sum_right = dfs(node.right)

            max_average = max(
                max_average,
                (sum_left + sum_right + node.val)
                / (elements_left + elements_right + 1),
            )

            return elements_left + elements_right + 1, sum_left + sum_right + node.val

        dfs(root)

        return max_average
