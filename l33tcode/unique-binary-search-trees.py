from functools import lru_cache


class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def dfs(node, left, right):
            if min(right, n) - max(left + 1, 0) == 1:
                return 1

            left_subtrees, right_subtrees = 0, 0
            for next_node in range(max(left + 1, 0), min(right, n)):
                if node != next_node:
                    if next_node > node:
                        right_subtrees += dfs(next_node, node, right)
                    else:
                        left_subtrees += dfs(next_node, left, node)

            return (right_subtrees or 1) * (left_subtrees or 1)

        count = dfs(float("-inf"), float("-inf"), float("+inf"))

        return count
