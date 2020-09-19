from typing import Dict, Set
from collections import Counter


class Solution:
    def longestAwesome(self, s: str) -> int:
        mask_pos: Dict[int, int] = {}

        mask = 0
        result = 0

        for pos in range(len(s)):
            mask ^= 1 << int(s[pos])

            result = max(result, pos - mask_pos.get(mask, pos))

            for shift in range(10):
                result = max(
                    result, pos - mask_pos.get(mask ^ (1 << shift), pos)
                )

            mask_pos.setdefault(mask, pos)

        return result

    def longestAwesomeBruteForce(self, s: str) -> int:
        result = 0

        for start in range(len(s)):
            count: Dict[str, int] = Counter()
            odd = 0

            for end in range(start, len(s)):
                count[s[end]] += 1

                if count[s[end]] & 1 > 0:
                    odd += 1
                else:
                    odd -= 1

                if odd <= 1:
                    result = max(result, end + 1 - start)

        return result
