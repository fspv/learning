from typing import Tuple
from collections import Counter
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        partial_sum = Counter([0])

        def dfs(node: TreeNode, cur_sum: int) -> int:
            if not node:
                return 0

            cur_sum += node.val

            result = partial_sum[cur_sum - sum]

            partial_sum[cur_sum] += 1


            result += dfs(node.left, cur_sum)
            result += dfs(node.right, cur_sum)

            partial_sum[cur_sum] -= 1

            return result

        result = 0

        return dfs(root, 0)

    def pathSumBruteForce(self, root: TreeNode, sum: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return {}, 0

            paths = Counter([node.val])

            paths_left, ways_left = dfs(node.left)
            paths_right, ways_right = dfs(node.right)

            for path_left, count_left in paths_left.items():
                paths[path_left + node.val] += count_left

            for path_right, count_right in paths_right.items():
                paths[path_right + node.val] += count_right

            return paths, ways_left + ways_right + paths[sum]

        _, ways = dfs(root)

        return ways
