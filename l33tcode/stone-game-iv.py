from functools import lru_cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = []

        for count in range(1, n + 1):
            square = count ** 2
            if square > n:
                break
            squares.append(square)

        @lru_cache(None)
        def dp(stones: int) -> bool:
            for square in squares:
                if square > stones:
                    break
                if not dp(stones - square):
                    return True

            return False

        return dp(n)
