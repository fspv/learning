from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        dp = [0] * (len(triangle) + 1)

        for row in reversed(range(len(triangle))):
            dp_old = dp
            dp = [float("+inf")] * (row + 1)

            for col in range(row + 1):
                dp[col] = min(dp_old[col], dp_old[col + 1],) + triangle[row][col]

        return dp[0]
