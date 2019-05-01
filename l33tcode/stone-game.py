from functools import lru_cache

class Solution:
    def stoneGame(self, piles):
        @lru_cache(None)
        def dp(left, right):
            if left > right:
                return 0

            first = (right - left + len(piles)) % 2 == 1

            if first:
                return max(
                    dp(left + 1, right) + piles[left],
                    dp(left, right - 1) + piles[right]
                )
            else:
                return min(
                    dp(left + 1, right) - piles[left],
                    dp(left, right - 1) - piles[right]
                )

        return dp(0, len(piles) - 1) > 0

    def stoneGameMathematical(self, piles):
        return True


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.stoneGame([1,2,3,4])
