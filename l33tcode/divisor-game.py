class Solution:
    def divisors(self, num):
        for cand in range(1, int(num ** 0.5) + 1, 1 if num % 2 == 0 else 2):
            if num % cand == 0:
                yield cand

    def divisorGame(self, N):
        return N % 2 == 0

    def divisorGameStraightForwardSolution(self, N):
        dp = [False] * (N + 1)

        for start in range(2, N + 1):
            for divisor in self.divisors(start):
                if not dp[start - divisor]:
                    dp[start] = True

        return dp[N]
