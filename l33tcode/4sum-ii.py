from collections import defaultdict
from functools import lru_cache


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        def construct_sums(*arrays):
            dp = {0: 1}

            for arr in arrays:
                new_dp = {}

                for prev_num, ways in dp.items():
                    for num in arr:
                        new_dp[num + prev_num] = new_dp.get(num + prev_num, 0) + ways

                dp = new_dp

            return dp

        sums_left = construct_sums(A, B)
        sums_right = construct_sums(C, D)

        count = 0
        for sum_left, count_left in sums_left.items():
            count += count_left * sums_right.get(-sum_left, 0)

        return count

    def fourSumCountTopDown(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        arr = [A, B, C, D]

        @lru_cache(None)
        def dfs(arr_pos, prev_sum):
            if arr_pos == len(arr):
                return int(prev_sum == 0)

            result = 0
            for pos in range(len(arr[arr_pos])):
                result += dfs(arr_pos + 1, prev_sum + arr[arr_pos][pos])

            return result

        return dfs(0, 0)
