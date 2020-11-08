from typing import List
from collections import Counter


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()

        left, right = 0, len(A) - 1

        result = -1

        while left < right:
            if A[left] + A[right] >= K:
                right -= 1
            else:
                result = max(result, A[left] + A[right])
                left += 1

        return result

    def twoSumLessThanKBruteForce(self, A: List[int], K: int) -> int:
        numbers = Counter(A)

        for two_sum in reversed(range(K)):
            for number in numbers.keys():
                numbers[number] -= 1

                if numbers.get(two_sum - number, 0) > 0:
                    return two_sum

                numbers[number] += 1

        return -1
