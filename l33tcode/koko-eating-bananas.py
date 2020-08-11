class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def can_eat(bananas: int) -> bool:
            pile = 0
            days = 0

            while pile < len(piles):
                days += piles[pile] // bananas
                if piles[pile] % bananas > 0:
                    days += 1

                pile += 1

                if days > H:
                    return False

            return True

        left, right = 1, max(piles)

        while left < right:
            middle = left + (right - left) // 2

            if not can_eat(middle):
                left = middle + 1
            else:
                right = middle

        return left
