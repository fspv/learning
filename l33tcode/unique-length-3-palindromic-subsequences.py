from typing import Counter, Dict, List


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counts: List[Dict[str]] = []
        counter: Counter[str] = Counter()

        first: Dict[str, int] = {}
        last: Dict[str, int] = {}

        for pos, char in enumerate(s):
            counter[char] += 1
            counts.append({k: v for k, v in counter.items()})

            if char not in first:
                first[char] = pos

            last[char] = pos

        subsequences = 0

        for char in counter.keys():
            if first[char] + 1 < last[char]:
                for chars_in_between, count in counts[last[char] - 1].items():
                    if count > counts[first[char]].get(chars_in_between, 0):
                        subsequences += 1

        return subsequences
