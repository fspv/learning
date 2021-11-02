from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left, right = 1, sum(sweetness) + 1

        def condition(mid: int) -> bool:
            """Can be splitted is less than k + 1 chunks"""
            total = 0
            count = 0

            for pos in range(len(sweetness)):
                total += sweetness[pos]

                if total >= mid:
                    count += 1
                    total = 0

            return count < k + 1

        while left < right:
            mid = (right - left) // 2 + left

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left - 1
