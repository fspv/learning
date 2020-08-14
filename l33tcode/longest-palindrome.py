from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        even, odd = 0, 0

        char_count = Counter()

        for char in s:
            char_count[char] += 1
            if char_count[char] % 2 == 0:
                odd -= 1
                even += 1
            else:
                odd += 1

        return even * 2 + int(odd > 0)
