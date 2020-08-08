from collections import Counter


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        shifts = Counter()
        alphabet_size = ord("z") - ord("a") + 1

        for pos in range(len(s)):
            if s[pos] != t[pos]:
                left, right = ord(s[pos]) - ord("a"), ord(t[pos]) - ord("a")

                diff = 0
                if left < right:
                    diff = right - left
                else:
                    diff = alphabet_size - (left - right)

                if diff + alphabet_size * shifts[diff] > k:
                    return False

                shifts[diff] += 1

        return True
