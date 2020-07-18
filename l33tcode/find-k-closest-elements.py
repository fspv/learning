import heapq
import random
from collections import deque


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bisect(arr, x):
            left, right = 0, len(arr) - 1
            result = 0

            while left < right:
                middle = (left + right) // 2
                if arr[middle] < x:
                    left = middle + 1
                    result = left
                elif arr[middle] > x:
                    right = middle - 1
                    result = right
                else:
                    return middle

            return result

        center = bisect(arr, x)

        left, right = max(center - k, 0), min(center + k, len(arr) - 1)

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left:right + 1]

    def findClosestElementsHeap(self, arr: List[int], k: int, x: int) -> List[int]:
        def construct_heap(heap, arr, x):
            for num in arr:
                heapq.heappush(heap, (abs(x - num), num))

        heap = []
        queue = deque()

        construct_heap(heap, arr, x)

        for _ in range(k):
            _, val = heapq.heappop(heap)

            if not queue or val <= queue[0]:
                queue.appendleft(val)
            else:
                queue.append(val)

        return list(queue)
