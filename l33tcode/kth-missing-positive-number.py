from typing import List


def missing_between(arr: List[int], left: int, right: int) -> int:
    if right >= len(arr):
        return 0

    if left == right:
        return 0

    return arr[right] - arr[left] + 1 - (right - left + 1)


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)

        def missing(pos: int) -> int:
            return arr[pos] - (pos + 1)

        while left < right:
            middle = left + (right - left) // 2

            if missing(middle) >= k:
                right = middle
            else:
                left = middle + 1

        if left == 0:
            return k

        return arr[left - 1] + (k - missing(left - 1))

    def findKthPositive1(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0

        if arr[0] > k:
            return k

        left, right = 0, len(arr) - 1

        last_less = 0
        missing_left = arr[0] - 1

        while left <= right:
            middle = (left + right) // 2

            missing = missing_between(arr, left, middle) + missing_left

            if missing < k:
                last_less = middle
                left = middle + 1
                missing_left = missing + missing_between(arr, middle, middle + 1)
            else:
                right = middle - 1

        return k - (missing_between(arr, 0, last_less) + arr[0] - 1) + arr[last_less]
