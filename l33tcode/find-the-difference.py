from itertools import chain
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0

        for char in chain(s, t):
            xor ^= ord(char)

        return chr(xor)

    def findTheDifferenceHasMap(self, s: str, t: str) -> str:
        count = Counter()

        for char in t:
            count[char] += 1

        for char in s:
            count[char] -= 1

        for char, char_count in count.items():
            if char_count > 0:
                return char
