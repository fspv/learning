import heapq
from typing import List, Tuple, Union
from functools import lru_cache


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        MAX_EFFICIENCY = max(efficiency) + 1
        MOD = 10 ** 9 + 7

        heap_speed: List[Tuple[int, int]] = []
        total = 0
        min_efficiency = MAX_EFFICIENCY
        max_performance = 0

        for pos, _ in sorted(enumerate(efficiency), key=lambda x: x[1], reverse=True):
            if len(heap_speed) == k:
                this_speed, this_pos = heapq.heappop(heap_speed)
                total -= this_speed

            heapq.heappush(heap_speed, (speed[pos], pos))
            min_efficiency = min(min_efficiency, efficiency[pos])
            total += speed[pos]

            max_performance = max(max_performance, (total * min_efficiency))

        return max_performance % MOD

    def maxPerformanceDPTopDown(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        # N ^ 3 -> TLE
        MAX_EFFICIENCY = max(efficiency) + 1
        MOD = 10 ** 9 + 7

        tmp = list(zip(efficiency, speed))
        tmp.sort()

        efficiency = list(map(lambda x: x[0], tmp))
        speed = list(map(lambda x: x[1], tmp))

        @lru_cache(None)
        def dp(pos: int, left: int) -> Tuple[int, int]:
            # return (sum of the path, min efficiency in the path)
            if left == 0:
                return (0, MAX_EFFICIENCY)

            if pos == len(speed):
                return (0, MAX_EFFICIENCY)

            # pick this and stop
            max_performance = speed[pos] * efficiency[pos]
            path_sum, min_efficiency = speed[pos], efficiency[pos]

            # pick this and continue
            for next_pos in range(pos + 1, len(speed)):
                path_sum_next, min_efficiency_next = dp(next_pos, left - 1)
                path_sum_this = path_sum_next + speed[pos]
                min_efficiency_this = min(min_efficiency_next, efficiency[pos])
                performance = path_sum_this * min_efficiency_this
                if performance > max_performance:
                    path_sum, min_efficiency = path_sum_this, min_efficiency_this
                    max_performance = performance

            return path_sum, min_efficiency

        max_performance = 0
        for pos in range(len(speed)):
            path_sum, min_efficiency = dp(pos, k)
            max_performance = max(max_performance, path_sum * min_efficiency)

        return max_performance % MOD
