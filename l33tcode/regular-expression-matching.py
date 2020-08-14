from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern_len = sum(map(lambda c: c != "*", p))
        string_len = len(s)
        dp = [[False] * (string_len + 1) for _ in range(pattern_len + 1)]
        dp[-1][-1] = True

        pattern = []
        can_repeat = [False] * pattern_len
        for char in p:
            if char == "*":
                can_repeat[len(pattern) - 1] = True
            else:
                pattern.append(char)

        for string_pos in reversed(range(string_len + 1)):
            for pattern_pos in reversed(range(pattern_len)):
                dp[pattern_pos][string_pos] = (
                    can_repeat[pattern_pos] and dp[pattern_pos + 1][string_pos]
                )

                if string_pos < string_len and pattern[pattern_pos] in (s[string_pos], "."):
                    dp[pattern_pos][string_pos] = (
                        dp[pattern_pos][string_pos]
                        or dp[pattern_pos + 1][string_pos + 1]
                        or (can_repeat[pattern_pos] and dp[pattern_pos][string_pos + 1])
                    )

        return dp[0][0]

    def isMatchTopDown(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(pattern_pos: int, string_pos: int) -> bool:
            def can_repeat(pattern_pos):
                return pattern_pos < (len(p) - 1) and p[pattern_pos + 1] == "*"

            if pattern_pos == len(p) and string_pos == len(s):
                return True

            if can_repeat(pattern_pos):
                if dfs(pattern_pos + 2, string_pos):
                    return True

            if pattern_pos == len(p) or string_pos == len(s):
                return False

            if p[pattern_pos] == s[string_pos] or p[pattern_pos] == ".":
                if can_repeat(pattern_pos):
                    if dfs(pattern_pos, string_pos + 1):
                        return True
                else:
                    if dfs(pattern_pos + 1, string_pos + 1):
                        return True
            else:
                return False

        return dfs(0, 0)
