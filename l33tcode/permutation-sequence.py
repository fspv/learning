import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        def perm(remain: list[int], count: int) -> list[str]:
            if count + 1 == k and len(remain) == 0:
                return result

            for num in remain.copy():
                remain.remove(num)
                result.append(str(num))
                if math.factorial(len(remain)) + count >= k:
                    return perm(remain, count)
                result.pop()
                count += math.factorial(len(remain))
                remain.append(num)
                remain.sort()

            return []

        return "".join(perm(list(range(1, n + 1)), 0))
