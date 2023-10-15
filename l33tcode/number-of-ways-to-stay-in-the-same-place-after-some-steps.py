from functools import cache

MOD = 10 ** 9 + 7


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(pos: int, steps: int) -> int:
            # Out of bounds
            if pos < 0 or pos >= arrLen:
                return 0

            # No more steps, are we at 0?
            if steps == 0:
                return int(pos == 0)

            # Try all the next step options
            return (
                # Left
                dp(pos - 1, steps - 1)
                # Stay
                + dp(pos, steps - 1)
                # Right
                + dp(pos + 1, steps - 1)
            ) % MOD

        return dp(0, steps)
