from functools import lru_cache


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [(")", -1)]

        max_length = 0

        for pos in range(len(s)):
            if s[pos] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                    start_pos = stack[-1][1]
                    max_length = max(max_length, pos - start_pos)
                else:
                    stack.append((")", pos))
            else:
                stack.append(("(", pos))

        return max_length

    def longestValidParenthesesBruteForce(self, s: str) -> int:
        @lru_cache(None)
        def dfs(pos: int, open_brackets: int, subarrays: int) -> int:
            if pos == len(s):
                return float("-inf") if open_brackets > 0 else 0

            max_len = 0 if open_brackets == 0 and subarrays > 0 else float("-inf")
            if s[pos] == ")":
                if open_brackets > 0:
                    max_len = max(max_len, dfs(pos + 1, open_brackets - 1, 1) + 1)
            else:
                max_len = max(max_len, dfs(pos + 1, open_brackets + 1, 1) + 1)

            if subarrays == 0:
                max_len = max(max_len, dfs(pos + 1, open_brackets, 0))

            return max_len

        return dfs(0, 0, 0)
