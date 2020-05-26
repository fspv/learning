from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(
            reversed(sorted([k * v for k, v in Counter(s).items()], key=len))
        )
