from typing import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        counter: Counter[str] = Counter()
        repeating = 0
        longest_substring = 0

        while right < len(s):
            while left + 1 < right and repeating > 0:
                counter[s[left]] -= 1

                if counter[s[left]] == 1:
                    repeating -= 1

                left += 1

            while repeating == 0:
                longest_substring = max(longest_substring, right - left)

                if right == len(s):
                    break

                counter[s[right]] += 1

                if counter[s[right]] == 2:
                    repeating += 1

                right += 1

        return longest_substring

    def lengthOfLongestSubstring1(self, s: str) -> int:
        str_hash_map = {}
        longest_substr = 0
        left = 0
        right = 0

        for n, c in enumerate(s):
            if c in str_hash_map:
                left = max(str_hash_map[c] + 1, left)

            str_hash_map[c] = n

            right = n

            longest_substr = max(longest_substr, right - left + 1)

        return longest_substr
