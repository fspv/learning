from typing import List
from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, roll_max: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(pos: int, rolls: int) -> int:
            if pos == 0:
                return 1

            count = 0
            for dice in range(6):
                roll = (rolls >> (dice * 4)) & 0x0F
                if roll < roll_max[dice]:
                    count += dp(pos - 1, (roll + 1) << (dice * 4)) % MOD

            return count % MOD

        return dp(n, 0)
