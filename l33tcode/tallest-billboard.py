from collections import defaultdict
from functools import lru_cache


class Solution:
    def tallestBillboardBottomUp2(self, rods: List[int]) -> int:
        max_sum = sum(rods) // 2
        dp = [[-1] * (max_sum + 1) for _ in range(max_sum + 1)]

        dp[0][0] = 0

        for rod in range(len(rods)):
            for left in range(max_sum + 1):
                for right in range(left, max_sum + 1):
                    if dp[left][right] == rod:
                        dp[left][right] = rod + 1
                        if (
                            left + rods[rod] <= max_sum
                            and dp[left + rods[rod]][right] != rod
                        ):
                            dp[left + rods[rod]][right] = rod + 1
                        if (
                            right + rods[rod] <= max_sum
                            and dp[left][right + rods[rod]] != rod
                        ):
                            dp[left][right + rods[rod]] = rod + 1

        for cur_sum in reversed(range(max_sum + 1)):
            if dp[cur_sum][cur_sum] > 0:
                return cur_sum

        return 0

    def tallestBillboardBottomUp1(self, rods: List[int]) -> int:
        max_len = sum(rods) // 2 + 1
        dp = [defaultdict(dict) for _ in range(len(rods) + 1)]
        dp[0][0][0] = True

        for rod in range(len(rods)):
            for left in dp[rod].keys():
                for right in dp[rod][left].keys():
                    if left <= max_len and right <= max_len:
                        dp[rod + 1][left][right] = True
                        dp[rod + 1][left + rods[rod]][right] = True
                        dp[rod + 1][-(left + rods[rod])][right] = True
                        dp[rod + 1][left][right + rods[rod]] = True

        result = 0

        for left in dp[-1].keys():
            for right in dp[-1][left].keys():
                if left == right:
                    result = max(result, left)

        return result

    def tallestBillboard(self, rods: List[int]) -> int:
        max_sum = sum(rods) // 2 + 1

        dp = defaultdict(int)
        dp[0] = 0

        for rod in range(len(rods)):
            dp_new = defaultdict(int)
            for total in dp:
                dp_new[total] = max(dp_new[total], dp[total])
                dp_new[total - rods[rod]] = max(dp_new[total - rods[rod]], dp[total])
                dp_new[total + rods[rod]] = max(
                    dp_new[total + rods[rod]], dp[total] + rods[rod]
                )
            dp = dp_new

        return dp[0]

    def tallestBillboardTopDownFast(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dfs(rod: int, total: int) -> int:
            if rod == len(rods):
                if total == 0:
                    return 0
                else:
                    return float("-inf")

            return max(
                dfs(rod + 1, total),
                dfs(rod + 1, total + rods[rod]) + rods[rod],
                dfs(rod + 1, total - rods[rod]),
            )

        return dfs(0, 0)

    def tallestBillboardTopDown(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dfs(rod: int, left: int, right: int) -> int:
            if rod == len(rods):
                if left == right:
                    return left
                else:
                    return 0

            return max(
                dfs(rod + 1, left + rods[rod], right),
                dfs(rod + 1, left, right + rods[rod]),
                dfs(rod + 1, left, right),
            )

        return dfs(0, 0, 0)
