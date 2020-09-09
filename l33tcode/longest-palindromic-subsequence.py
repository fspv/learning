from itertools import chain
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in s]

        for left in reversed(range(len(s))):
            for right in range(left, len(s)):
                if left == right:
                    dp[left][right] = 1
                elif s[left] != s[right]:
                    dp[left][right] = max(
                        dp[left + 1][right], dp[left][right - 1],
                    )
                else:
                    dp[left][right] = dp[left + 1][right - 1] + 2

        return max(chain(*dp))

    def longestPalindromeSubseqTopDown1(self, s: str) -> int:
        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0

            if left == right:
                return 1

            if s[left] != s[right]:
                return max(
                    dfs(left + 1, right),
                    dfs(left, right - 1),
                )

            return dfs(left + 1, right - 1) + 2

        max_palindrome = 0

        for left in range(len(s)):
            for right in range(left, len(s)):
                max_palindrome = max(max_palindrome, dfs(left, right))

        return max_palindrome

    def longestPalindromeSubseqTopDown2(self, s: str) -> int:
        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if left < 0 or right >= len(s):
                return 0

            if s[left] != s[right]:
                return max(
                    dfs(left - 1, right),
                    dfs(left, right + 1),
                )

            return dfs(left - 1, right + 1) + 2

        max_palindrome = 0

        for pos in range(len(s)):
            max_palindrome = max(max_palindrome, dfs(pos, pos) - 1)

        for pos in range(1, len(s)):
            max_palindrome = max(max_palindrome, dfs(pos - 1, pos))

        return max_palindrome
