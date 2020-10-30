from typing import List
from functools import lru_cache


class Solution:
    def findLength(self, left: List[int], right: List[int]) -> int:
        max_length = 0
        dp = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]

        for left_pos in reversed(range(len(left))):
            for right_pos in reversed(range(len(right))):
                if left[left_pos] == right[right_pos]:
                    dp[left_pos][right_pos] = dp[left_pos + 1][right_pos + 1] + 1
                    max_length = max(dp[left_pos][right_pos], max_length)

        return max_length

    def findLengthTopDown(self, left: List[int], right: List[int]) -> int:
        max_length = 0

        @lru_cache(None)
        def dp(pos_left: int, pos_right: int) -> int:
            nonlocal max_length

            if pos_left == len(left) or pos_right == len(right):
                return 0

            dp(pos_left + 1, pos_right)
            dp(pos_left, pos_right + 1)

            if left[pos_left] == right[pos_right]:
                length = dp(pos_left + 1, pos_right + 1) + 1
                max_length = max(length, max_length)

                return length

            return 0

        dp(0, 0)

        return max_length
