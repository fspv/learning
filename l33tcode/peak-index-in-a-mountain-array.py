from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 1, len(A) - 1

        def uphill(pos: int) -> bool:
            # `pos` will never be the last element, because
            # the only way to achieve it is to have
            # `left == right`, which is guaranteed to be
            # impossible by the loop condition `left < right`
            return A[pos] < A[pos + 1]

        while left < right:
            mid = left + (right - left) // 2

            if uphill(mid):
                left = mid + 1
            else:
                right = mid

        return left
