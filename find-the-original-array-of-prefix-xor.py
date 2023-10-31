from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i - 1] ^ pref[i] for i in range(1, len(pref))]
