from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one_bits(num: int) -> int:
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        return sorted(arr, key=lambda x: (count_one_bits(x), x))
