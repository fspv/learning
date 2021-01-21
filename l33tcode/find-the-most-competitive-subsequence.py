import heapq
from typing import List, Tuple


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack: List[int] = []

        can_drop = len(nums) - k

        for num in nums:
            while stack and stack[-1] > num and can_drop > 0:
                stack.pop()
                can_drop -= 1

            stack.append(num)

        return stack[:k]

    def mostCompetitiveHeap(self, nums: List[int], k: int) -> List[int]:
        left = -1
        heap: List[Tuple[int, int]] = []  # value, pos
        result: List[int] = []

        for right in range(len(nums) - k):
            heapq.heappush(heap, (nums[right], right))

        for right in range(len(nums) - k, len(nums)):
            heapq.heappush(heap, (nums[right], right))

            min_val, min_pos = heapq.heappop(heap)

            while min_pos <= left:
                min_val, min_pos = heapq.heappop(heap)

            left = min_pos
            result.append(min_val)

        return result
