from functools import lru_cache


class Solution:
    def canIWin(self, max_int: int, total: int) -> bool:
        @lru_cache(None)
        def dp(bitmask: int, left: int) -> bool:
            if left <= 0:
                return False

            for num in range(1, max_int + 1):
                if bitmask & (1 << num) == 0:
                    if not dp(bitmask | (1 << num), left - num):
                        return True

            return False

        if total == 0:
            return True

        if total > max_int * (max_int + 1) // 2:
            return False

        return dp(0, total)
