from typing import Set, Tuple


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # O(K^2) solution. We can do better with O(K)
        mod = 1 % K
        mod_total = mod
        count = 1

        seen: Set[Tuple[int, int]] = set()

        while mod_total != 0:
            mod = (mod * 10) % K
            mod_total = (mod_total + mod) % K

            if (mod, mod_total) in seen:
                return -1
            seen.add((mod, mod_total))

            count += 1

        return count
