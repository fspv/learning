from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:  # Mem limit exceeded otherwise
            return 1.0

        n = n // 25 + (1 if n % 25 > 0 else 0)

        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5

        for A in range(1, n + 1):
            for B in range(1, n + 1):
                dp[0][B] = 1
                for serve_A, serve_B in ((4, 0), (3, 1), (2, 2), (1, 3)):
                    dp[A][B] += dp[max(A - serve_A, 0)][max(B - serve_B, 0)] * 0.25

        return dp[n][n]

    def soupServingsTopDown(self, n: int) -> float:
        if n > 4800:  # Stack limit execeeded otherwise
            return 1.0

        n = n // 25 + (1 if n % 25 > 0 else 0)

        @lru_cache(None)
        def dp(A: int, B: int) -> float:
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1
            if B <= 0:
                return 0

            probability = 0

            for serve_A, serve_B in ((4, 0), (3, 1), (2, 2), (1, 3)):
                probability += dp(A - serve_A, B - serve_B) * 0.25

            return probability

        return dp(n, n)
