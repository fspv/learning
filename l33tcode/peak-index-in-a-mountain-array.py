class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 1, len(A) - 2

        def condition(pos: int) -> bool:
            return A[pos] < A[pos + 1]

        while left < right:
            middle = left + (right - left) // 2

            if condition(middle):
                left = middle + 1
            else:
                right = middle

        return left
