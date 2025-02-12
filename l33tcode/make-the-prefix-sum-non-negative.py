import heapq


class Solution:
    def makePrefSumNonNegative(self, nums: list[int]) -> int:
        heap: list[int] = []
        prefix_sum = 0
        swaps = 0

        for num in nums:
            if num < 0:
                heapq.heappush(heap, num)

            prefix_sum += num

            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(heap)
                swaps += 1

        return swaps
