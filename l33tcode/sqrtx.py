class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared - x == 0:
                return mid
            elif squared - x < 0:
                left = mid + 1
            else:
                right = mid - 1

        return min(left, right)
