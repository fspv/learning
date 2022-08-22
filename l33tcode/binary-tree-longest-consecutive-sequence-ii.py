from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_overall = 0

        def dfs(node: TreeNode) -> Tuple[int, int]:
            """
            fwd - starts at this number
            back - ends with this number
            """
            nonlocal max_overall

            # Accumulates longest subsequences passing through this point
            # (but not necessarily terminating here)
            increasing, descreasing = 1, 1

            # Stores the longest subsequence from below, terminating at this node
            max_fwd, max_back = 1, 1

            if node.left:
                max_next_fwd, max_next_back = dfs(node.left)

                if node.left.val - node.val == 1:
                    descreasing += max_next_fwd
                    max_fwd = max(max_fwd, max_next_fwd + 1)
                elif node.left.val - node.val == -1:
                    increasing += max_next_back
                    max_back = max(max_back, max_next_back + 1)

            if node.right:
                max_next_fwd, max_next_back = dfs(node.right)

                if node.right.val - node.val == 1:
                    increasing += max_next_fwd
                    max_fwd = max(max_fwd, max_next_fwd + 1)
                elif node.right.val - node.val == -1:
                    descreasing += max_next_back
                    max_back = max(max_back, max_next_back + 1)

            max_overall = max(max_overall, increasing, descreasing)

            return (max_fwd, max_back)

        if root:
            dfs(root)

        return max_overall

    def longestConsecutiveBruteForce(self, root: Optional[TreeNode]) -> int:
        max_overall = 0

        def backtrack(node: TreeNode, direction: bool) -> int:
            max_len = 1

            if node.left and (
                (node.left.val - node.val) == 1
                if direction
                else (node.left.val - node.val) == -1
            ):
                max_len = max(max_len, backtrack(node.left, direction) + 1)

            if node.right and (
                (node.right.val - node.val) == 1
                if direction
                else (node.right.val - node.val) == -1
            ):
                max_len = max(max_len, backtrack(node.right, direction) + 1)

            return max_len

        def dfs(node: TreeNode) -> None:
            nonlocal max_overall

            max_left_fw, max_left_back = 0, 0
            max_right_fw, max_right_back = 0, 0

            if node.left:
                if (node.left.val - node.val) == 1:
                    max_left_fw = backtrack(node.left, True)

                if (node.left.val - node.val) == -1:
                    max_left_back = backtrack(node.left, False)

                dfs(node.left)
            if node.right:
                if (node.right.val - node.val) == 1:
                    max_right_fw = backtrack(node.right, True)

                if (node.right.val - node.val) == -1:
                    max_right_back = backtrack(node.right, False)

                dfs(node.right)

            max_overall = max(
                max_overall,
                max_right_fw + max_left_back + 1,
                max_left_fw + max_right_back + 1,
            )

        if root:
            dfs(root)

        return max_overall
