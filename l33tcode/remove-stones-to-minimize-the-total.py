import heapq
from functools import lru_cache
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap: List[int] = []
        for pile in piles:
            heapq.heappush(heap, -pile)

        result = 0

        for _ in range(k):
            if not heap:
                break

            top = -heapq.heappop(heap)

            result += top // 2

            left = top - top // 2

            if left > 0:
                heapq.heappush(heap, -left)

        return sum(piles) - result

    def minStoneSumDP(self, piles: List[int], k: int) -> int:
        total = sum(piles)

        @lru_cache(None)
        def dp(pile: int, operations: int) -> int:
            nonlocal total

            if pile == len(piles):
                if operations > 0:
                    return 0
                else:
                    return 0

            result = 0

            stones = piles[pile]
            removed = 0

            for op in range(operations + 1):
                result = max(result, dp(pile + 1, operations - op) + removed)

                removed += stones // 2
                stones -= stones // 2

            return result

        return total - dp(0, k)
