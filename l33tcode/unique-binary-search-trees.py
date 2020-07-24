from functools import lru_cache


class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def dfs(nodes):
            if nodes == 0:
                return 1

            count = 0
            for split in range(nodes):
                left_subtrees = dfs(split)
                right_subtrees = dfs(nodes - split - 1)
                count += left_subtrees * right_subtrees

            return count

        return dfs(n)
