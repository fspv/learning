from typing import DefaultDict
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, string: str) -> int:
        begin = 0
        seen_last: DefaultDict[str, int] = defaultdict(lambda: -1)
        longest_substring = 0

        for pos in range(len(string)):
            seen_last[string[pos]] = pos

            if len(seen_last) > 2:
                earliest_key = min(seen_last.keys(), key=lambda key: seen_last[key])
                begin = seen_last[earliest_key] + 1
                seen_last.pop(earliest_key)

            longest_substring = max(longest_substring, pos - begin + 1)

        return longest_substring
