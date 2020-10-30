from functools import lru_cache


class Solution:
    def minWindow(self, string: str, pattern: str) -> str:
        min_window_length = len(string) + 1
        min_window_start, min_window_end = 0, len(string) + 1
        max_pos = len(string) * 2 + 1

        dp = [max_pos] * (len(pattern) + 1)
        dp[-1] = len(string)

        for string_pos in reversed(range(len(string))):
            dp_old = dp
            dp = [max_pos] * min(len(pattern), string_pos + 1)
            dp.append(string_pos)
            for pattern_pos in reversed(range(min(len(pattern), string_pos + 1))):
                if string[string_pos] == pattern[pattern_pos]:
                    dp[pattern_pos] = dp_old[pattern_pos + 1]
                else:
                    dp[pattern_pos] = dp_old[pattern_pos]

            min_end = dp[0]

            if min_end - string_pos <= min_window_length:
                min_window_length = min_end - string_pos
                min_window_start, min_window_end = string_pos, min_end

        if min_window_length > len(string):
            return ""

        return string[min_window_start:min_window_end]

    def minWindowTopDown(self, string: str, pattern: str) -> str:
        min_window_length = len(string) + 1
        min_window_start, min_window_end = 0, len(string) + 1

        @lru_cache(None)
        def dp(string_pos: int, pattern_pos: int) -> int:
            nonlocal min_window_length
            nonlocal min_window_start, min_window_end

            if string_pos == len(string) or pattern_pos == len(pattern):
                if string_pos == len(string) and pattern_pos < len(pattern):
                    return len(string) + 1
                else:
                    return string_pos

            if string[string_pos] == pattern[pattern_pos]:
                return dp(string_pos + 1, pattern_pos + 1)
            else:
                return dp(string_pos + 1, pattern_pos)

            return min_end

        for string_pos in range(len(string) - (len(pattern) - 1)):
            if string[string_pos] == pattern[0]:
                min_end = dp(string_pos + 1, 1)

                if min_end - string_pos < min_window_length:
                    min_window_length = min_end - string_pos
                    min_window_start, min_window_end = string_pos, min_end

        if min_window_length > len(string):
            return ""

        return string[min_window_start:min_window_end]
