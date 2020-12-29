from typing import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start, end = 0, 0
        counter: Counter[str] = Counter()
        count = 0
        longest_substring = 0

        while end < len(s):
            while count <= k:
                longest_substring = max(longest_substring, end - start)

                if end == len(s):
                    break

                counter[s[end]] += 1
                if counter[s[end]] == 1:
                    count += 1

                end += 1

            counter[s[start]] -= 1
            if counter[s[start]] == 0:
                count -= 1

            start += 1

        return longest_substring
