import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1

        def can_arrive(speed: int) -> bool:
            remaining = hour

            for pos in range(len(dist) - 1):
                remaining -= math.ceil(dist[pos] / speed)
                if remaining <= 0:
                    return False

            # Round because `2.01 % 1 == 0.009999999999999787`
            return round(remaining, 2) >= dist[-1] / speed

        # Guarantees arrival on time
        max_speed = math.ceil(max(dist) / ((hour % 1) or 1))
        left, right = 1, max_speed

        while left < right:
            mid = left + (right - left) // 2

            if not can_arrive(mid):
                left = mid + 1
            else:
                right = mid

        return left
