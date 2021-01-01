from typing import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter: Counter[str] = Counter()
        odd = 0

        for char in s:
            counter[char] += 1
            if counter[char] % 2 == 1:
                odd += 1
            else:
                odd -= 1

        return odd < 2
