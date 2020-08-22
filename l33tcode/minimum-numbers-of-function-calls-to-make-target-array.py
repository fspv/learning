from typing import List, Tuple
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def ones(num: int) -> Tuple[int, int]:
            ones_count, count = 0, 0

            while num > 0:
                count += 1
                ones_count += num & 1
                num >>= 1

            return ones_count, count - 1

        operations = 0

        max_log2 = 0

        for num in nums:
            if num > 0:
                ones_count, count = ones(num)
                max_log2 = max(count, max_log2)
                operations += ones_count

        operations += max_log2

        return operations
