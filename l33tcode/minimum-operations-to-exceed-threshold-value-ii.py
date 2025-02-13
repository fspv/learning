import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        ops = 0

        while (first := heapq.heappop(nums)) < k:
            second = heapq.heappop(nums)
            heapq.heappush(nums, min(first, second) * 2 + max(first, second))
            ops += 1

        return ops
