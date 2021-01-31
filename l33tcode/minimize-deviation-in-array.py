import heapq
from typing import List, Tuple


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap: List[Tuple[int, int]] = []
        min_num = max(nums)
        max_num = 0
        for num in nums:
            if num & 1 == 0:
                limit = num
                while num & 1 == 0:
                    num >>= 1
            else:
                limit = num << 1

            min_num = min(min_num, num)
            max_num = max(max_num, num)
            heapq.heappush(heap, (num, limit))

        min_diff = max_num - min_num

        while True:
            num, limit = heapq.heappop(heap)

            min_diff = min(min_diff, max_num - num)

            if num < limit:
                max_num = max(max_num, num << 1)
                heapq.heappush(heap, (num << 1, limit))
            else:
                break

        return min_diff
