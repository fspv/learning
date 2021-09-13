from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter: Counter[str] = Counter(text)
        counter_baloon: Counter[str] = Counter("balloon")

        return min(
            counter[char] // counter_baloon[char] for char in counter_baloon.keys()
        )
