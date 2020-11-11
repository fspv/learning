import heapq
from functools import lru_cache
from collections import deque


class Solution:
    def reachingPoints(
        self, source_x: int, source_y: int, target_x: int, target_y: int
    ) -> bool:
        if target_x < source_x or target_y < source_y:
            return False

        while target_y >= source_y and target_x >= source_x:
            if (target_x, target_y) == (source_x, source_y):
                return True

            if target_x > target_y:
                target_x %= target_y
            elif target_x < target_y:
                target_y %= target_x
            else:
                return False

        if target_x < source_x and target_y == source_y:
            return (source_x - target_x) % target_y == 0

        if target_y < source_y and target_x == source_x:
            return (source_y - target_y) % target_x == 0

        return False

    def reachingPointsRecursive(
        self, source_x: int, source_y: int, target_x: int, target_y: int
    ) -> bool:
        @lru_cache(None)
        def dp(x: int, y: int) -> bool:
            if (x, y) == (target_x, target_y):
                return True

            if x > target_x or y > target_y:
                return False

            if dp(x + y, y):
                return True

            if dp(x, x + y):
                return True

            return False

        return dp(source_x, source_y)
