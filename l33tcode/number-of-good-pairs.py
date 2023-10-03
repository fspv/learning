from typing import Counter, List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter: Counter[int] = Counter()

        result = 0

        for num in nums:
            result += counter[num]
            counter[num] += 1

        return result
