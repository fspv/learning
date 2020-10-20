from functools import lru_cache


class Solution:
    def maxScore(self, card_points: List[int], cards: int) -> int:
        total = sum(card_points)

        if cards == len(card_points):
            return total

        range_sum = 0
        min_range_sum = total

        for pos in range(len(card_points)):
            if pos >= (len(card_points) - cards):
                min_range_sum = min(min_range_sum, range_sum)
                range_sum -= card_points[pos - (len(card_points) - cards)]

            range_sum += card_points[pos]

        min_range_sum = min(min_range_sum, range_sum)

        return total - min_range_sum

    def maxScoreBruteForce(self, card_points: List[int], cards: int) -> int:
        @lru_cache(None)
        def dp(start: int, end: int, cards: int) -> int:
            if cards == 0:
                return 0

            if start > end:
                return 0

            return max(
                dp(start + 1, end, cards - 1) + card_points[start],
                dp(start, end - 1, cards - 1) + card_points[end],
            )

        return dp(0, len(card_points) - 1, cards)
