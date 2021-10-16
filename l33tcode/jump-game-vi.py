import heapq
from typing import List, Tuple


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        heap: List[Tuple[int, int]] = [(0, -k - 1)]

        for pos in range(0, len(nums) - 1):
            max_sum = -heap[0][0] + nums[pos]

            heapq.heappush(heap, (-max_sum, pos))

            while heap[0][1] < pos - k + 1:
                heapq.heappop(heap)

        return -heap[0][0] + nums[-1]

    def maxResultDPBottomUp(self, nums: List[int], k: int) -> int:
        dp: List[float] = [float("-inf")] * len(nums)

        dp[0] = nums[0]

        for pos in range(len(nums)):
            for jump_to in range(pos + 1, min(pos + k + 1, len(nums))):
                dp[jump_to] = max(dp[jump_to], dp[pos] + nums[jump_to])

        return int(dp[-1])
