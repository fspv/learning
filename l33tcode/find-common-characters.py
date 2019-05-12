from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        prev = None

        for word in A:
            cur = Counter()
            for l in word:
                cur[l] += 1

            if prev is None:
                prev = cur
            else:
                for l in list(prev.keys()):
                    if l in cur:
                        prev[l] = min(prev[l], cur[l])
                    else:
                        prev.pop(l)

        result = []

        for l in prev:
            while prev[l] > 0:
                result.append(l)
                prev[l] -= 1

        return result
