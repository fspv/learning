from typing import Optional, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_deepest_leaves(root: TreeNode) -> Set[int]:
            def max_depth_dfs(node: TreeNode) -> int:
                return max(
                    (max_depth_dfs(node.left) + 1 if node.left else 0),
                    (max_depth_dfs(node.right) + 1 if node.right else 0),
                )

            max_depth = max_depth_dfs(root)

            deepest_leaves: Set[int] = set()

            def deepest_leaves_dfs(node: TreeNode, depth: int) -> None:
                if node.left:
                    deepest_leaves_dfs(node.left, depth + 1)

                if node.right:
                    deepest_leaves_dfs(node.right, depth + 1)

                if depth == max_depth:
                    deepest_leaves.add(node.val)

            deepest_leaves_dfs(root, 0)

            return deepest_leaves

        if not root:
            return None

        deepest_leaves = find_deepest_leaves(root)

        lowest_common_ancestor: Optional[TreeNode] = None

        def dfs(node: TreeNode) -> bool:
            nonlocal lowest_common_ancestor

            left, right = False, False

            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)

            if (left and right) or (node.val in deepest_leaves):
                lowest_common_ancestor = node

            if left or right or (node.val in deepest_leaves):
                return True

            return False

        dfs(root)

        return lowest_common_ancestor
