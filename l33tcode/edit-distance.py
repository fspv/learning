from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for row in range(len(dp)):
            for col in range(len(dp[row])):
                if row > 0 and col > 0:
                    dp[row][col] = dp[row - 1][col - 1] + int(word1[row - 1] != word2[col - 1])
                else:
                    dp[row][col] = max(row, col)

                if row > 0:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col] + 1)

                if col > 0:
                    dp[row][col] = min(dp[row][col], dp[row][col - 1] + 1)

        return dp[-1][-1]

    def minDistanceRecursive(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def distance(ptr1, ptr2):
            if ptr1 == len(word1):
                return len(word2) - ptr2

            if ptr2 == len(word2):
                return len(word1) - ptr1

            if word1[ptr1] == word2[ptr2]:
                return distance(ptr1 + 1, ptr2 + 1)

            insert = 1 + distance(ptr1, ptr2 + 1)
            delete = 1 + distance(ptr1 + 1, ptr2)
            replace = 1 + distance(ptr1 + 1, ptr2 + 1)

            return min(insert, delete, replace)

        return distance(0, 0)
