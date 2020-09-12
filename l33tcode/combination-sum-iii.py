from typing import List, Tuple


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [[False] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = True

        for step in range(k):
            for num_first in range(n + 1):
                for num_second in range(10):
                    if num_first + num_second <= n:
                        dp[step + 1][num_first + num_second] = (
                            dp[step + 1][num_first + num_second] or dp[step][num_first]
                        )

        result = []

        def dfs(number: int, step: int, path: List[int]) -> None:
            if number < 0:
                return

            if step < 0:
                return

            if not dp[step][number]:
                return

            if number == 0 and step == 0:
                result.append(path.copy())

            for next_number in range(path[-1] + 1 if path else 1, min(number + 1, 10)):
                path.append(next_number)
                dfs(number - next_number, step - 1, path)
                path.pop()

        dfs(n, k, [])

        return result

    def combinationSum3TopDown(self, k: int, n: int) -> List[List[int]]:
        def dfs(
            number: int, total: int, steps: int, path: List[int]
        ) -> List[List[int]]:
            if steps > k:
                return []

            if total > n:
                return []

            if total == n and steps == k:
                return [path.copy()]

            if number > 9:
                return []

            result = []

            path.append(number)
            result += dfs(number + 1, total + number, steps + 1, path)
            path.pop()

            result += dfs(number + 1, total, steps, path)

            return result

        return dfs(1, 0, 0, [])
