from typing import List, Dict, Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter: Counter[int] = Counter(nums)

        operations = 0

        for num in nums:
            if counter[num] > 0:
                counter[num] -= 1

                if counter[k - num] > 0:
                    operations += 1
                    counter[k - num] -= 1

        return operations
