class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_count = 0
        max_vowels_count = 0
        vowels = {"a", "e", "i", "o", "u"}

        for pos in range(len(s)):
            if pos >= k:
                if s[pos - k] in vowels:
                    vowels_count -= 1

            if s[pos] in vowels:
                vowels_count += 1

            max_vowels_count = max(max_vowels_count, vowels_count)

        return max_vowels_count


