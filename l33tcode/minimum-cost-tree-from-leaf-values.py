from typing import Tuple
from functools import lru_cache


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float("+inf")]

        result = 0

        for num in arr:
            keep = 0
            while stack[-1] <= num:
                result += stack.pop() * min(stack[-1], num)

            stack.append(num)

        while len(stack) > 2:
            result += stack.pop() * stack[-1]

        return result

    def mctFromLeafValuesDPBottomUp(self, arr: List[int]) -> int:
        dp_size = (len(arr) + 1)
        dp = [
            [(float("+inf"), float("-inf"))] * dp_size for _ in range(dp_size)
        ]

        for pos in range(dp_size):
            for left in range(dp_size):
                right = left + pos

                if right == dp_size:
                    break

                if left + 1 == right:
                    dp[left][right] = (0, arr[left])

                for middle in range(left + 1, right):
                    left_sum, left_max  = dp[left][middle]
                    right_sum, right_max  = dp[middle][right]

                    cur_sum = left_sum + right_sum + left_max * right_max

                    if cur_sum < dp[left][right][0]:
                        dp[left][right] = (cur_sum, max(left_max, right_max))

        return dp[0][len(arr)][0]

    def mctFromLeafValuesDPTopDown(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dfs(left: int, right: int) -> Tuple[int, int]:
            if left == right:
                return float("+inf"), float("+inf")

            if left + 1 == right:
                return arr[left], 0

            max_leaf = arr[left]
            min_sum = float("+inf")

            for middle in range(left + 1, right):
                left_max, left_sum = dfs(left, middle)
                right_max, right_sum = dfs(middle, right)
                max_leaf = max(left_max, right_max)

                cur_sum = left_sum + right_sum + left_max * right_max
                if cur_sum < min_sum:
                    min_sum = cur_sum

            return max_leaf, min_sum

        return dfs(0, len(arr))[1]
