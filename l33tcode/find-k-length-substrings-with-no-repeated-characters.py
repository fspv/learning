from typing import Set


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        left, right = 0, 0

        count = 0
        seen: Set[str] = set()

        while right < len(S):
            while S[right] in seen:
                seen.discard(S[left])
                left += 1

            seen.add(S[right])

            right += 1

            if right - left >= K:
                count += 1

        return count
