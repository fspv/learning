import heapq
from typing import List, Tuple


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap: List[Tuple[int, int]] = []  # (-max_sum, pos)
        max_sum = nums[0]

        for pos, num in enumerate(nums):
            while heap and heap[0][1] < pos - k:
                heapq.heappop(heap)

            max_prev_sum = max(0, -heap[0][0]) if heap else 0
            heapq.heappush(heap, (-(max_prev_sum + num), pos))
            max_sum = max(max_sum, max_prev_sum + num)

        return max_sum
