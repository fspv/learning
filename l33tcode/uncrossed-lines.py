class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        left, right = A, B
        dp = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]

        for left_pos in range(1, len(left) + 1):
            for right_pos in range(1, len(right) + 1):
                if left[left_pos - 1] == right[right_pos - 1]:
                    dp[left_pos][right_pos] = max(
                        dp[left_pos - 1][right_pos - 1] + 1,
                        dp[left_pos - 1][right_pos],
                        dp[left_pos][right_pos - 1],
                    )
                else:
                    dp[left_pos][right_pos] = max(
                        dp[left_pos - 1][right_pos - 1],
                        dp[left_pos - 1][right_pos],
                        dp[left_pos][right_pos - 1],
                    )

        return dp[len(left)][len(right)]

    def maxUncrossedLinesRecursiveCached(self, A: List[int], B: List[int]) -> int:
        left, right = A, B
        cache = {}

        def dfs(ptr_left: int, ptr_right: int, lines: int) -> None:
            if ptr_left >= len(left) or ptr_right >= len(right):
                return lines

            if (ptr_left, ptr_right) in cache:
                return cache[(ptr_left, ptr_right)]

            max_lines = lines
            if left[ptr_left] == right[ptr_right]:
                max_lines = max(max_lines, dfs(ptr_left + 1, ptr_right + 1, lines + 1))
            else:
                max_lines = max(max_lines, dfs(ptr_left, ptr_right + 1, lines))
                max_lines = max(max_lines, dfs(ptr_left + 1, ptr_right, lines))

            cache[(ptr_left, ptr_right)] = max_lines
            return max_lines

        return dfs(0, 0, 0)
