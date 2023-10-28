from functools import cache

MOD = 10 ** 9 + 7


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follow_map = {
            "a": {"e"},
            "e": {"a", "i"},
            "i": {"a", "e", "o", "u"},
            "o": {"i", "u"},
            "u": {"a"},
        }

        @cache
        def dp(pos: int, vowel: str) -> int:
            if pos == n - 1:
                return 1

            count = 0

            for following_vowel in follow_map[vowel]:
                count += dp(pos + 1, following_vowel) % MOD

            return count % MOD

        return sum([dp(0, vowel) for vowel in follow_map.keys()]) % MOD
