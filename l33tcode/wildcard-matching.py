from functools import lru_cache


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]
        dp[-1][-1] = True

        pattern_pos = len(pattern) - 1

        while pattern_pos >= 0 and pattern[pattern_pos] == "*":
            dp[-1][pattern_pos] = True
            pattern_pos -= 1

        for string_pos in reversed(range(len(string))):
            for pattern_pos in reversed(range(len(pattern))):
                if pattern[pattern_pos] == "*":
                    dp[string_pos][pattern_pos] = (
                        dp[string_pos + 1][pattern_pos + 1]
                        or dp[string_pos + 1][pattern_pos]
                        or dp[string_pos][pattern_pos + 1]
                    )
                elif pattern[pattern_pos] == "?":
                    dp[string_pos][pattern_pos] = dp[string_pos + 1][pattern_pos + 1]
                elif pattern[pattern_pos] == string[string_pos]:
                    dp[string_pos][pattern_pos] = dp[string_pos + 1][pattern_pos + 1]

        return dp[0][0]

    def isMatchTopDown(self, string: str, pattern: str) -> bool:
        @lru_cache(None)
        def dp(string_pos: int, pattern_pos: int) -> bool:
            if string_pos == len(string):
                while pattern_pos < len(pattern) and pattern[pattern_pos] == "*":
                    pattern_pos += 1
                return pattern_pos == len(pattern)

            if pattern_pos == len(pattern):
                return False

            result = False
            if pattern[pattern_pos] == "*":
                result = result or dp(string_pos + 1, pattern_pos + 1)
                result = result or dp(string_pos + 1, pattern_pos)
                result = result or dp(string_pos, pattern_pos + 1)
            elif pattern[pattern_pos] == "?":
                result = result or dp(string_pos + 1, pattern_pos + 1)
            elif pattern[pattern_pos] == string[string_pos]:
                result = result or dp(string_pos + 1, pattern_pos + 1)

            return result

        return dp(0, 0)
