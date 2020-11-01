class Solution:
    def maxA(self, N: int) -> int:
        dp = [0] * (N + 3)

        for pos in range(3, N + 3):
            dp[pos] = max(
                dp[pos - 1] + 1,
                dp[pos - 3] * 2,
                dp[pos - 4] * 3,
                dp[pos - 5] * 4,
            )

        return dp[-1]

    def maxABruteForce(self, N: int) -> int:
        def dp(pos: int, printed_size: int, selected: bool, buffer_size: int) -> int:
            if pos == N:
                return printed_size

            return max(
                dp(pos + 1, printed_size + 1, False, 0),  # add 1 character
                dp(pos + 1, printed_size, True, 0),  # select
                dp(pos + 1, printed_size, False, printed_size) if selected else 0,  # copy into buffer
                dp(pos + 1, printed_size + buffer_size, False, buffer_size),  # paste buffer
            )

        return dp(0, 0, False, 0)
