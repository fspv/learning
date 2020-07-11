class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cache = set()
        power = 2 ** k
        for pos in range(len(s) - k + 1):
            cache.add(s[pos:(pos + k)])
            if len(cache) == power:
                return True

        return False
