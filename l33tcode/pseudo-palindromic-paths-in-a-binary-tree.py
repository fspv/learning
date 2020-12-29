from typing import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0

        counter: Counter[int] = Counter()

        def dfs(node: TreeNode, odd: int) -> int:
            counter[node.val] += 1

            if counter[node.val] % 2 == 1:
                odd += 1
            else:
                odd -= 1

            if not node.left and not node.right:
                if odd < 2:
                    counter[node.val] -= 1
                    return 1
                else:
                    counter[node.val] -= 1
                    return 0

            count = 0

            if node.left:
                count += dfs(node.left, odd)

            if node.right:
                count += dfs(node.right, odd)

            counter[node.val] -= 1

            return count

        return dfs(root, 0)
