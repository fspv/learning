from typing import List


def bisect_pivot(array: List[int]) -> int:
    left, right = 0, len(array)

    while right > 0 and array[right - 1] == array[0]:
        right -= 1

    while left < right:
        middle = left + (right - left) // 2

        if array[middle] < array[0]:
            right = middle
        else:
            left = middle + 1

    return left % len(array)


def bisect_target(array: List[int], pivot: int, target: int) -> int:
    left, right = 0, len(array) - 1

    while left < right:
        middle = left + (right - left) // 2

        if array[(middle + pivot) % len(array)] >= target:
            right = middle
        else:
            left = middle + 1

    return (left + pivot) % len(array)


def check_target_valid(array: List[int], target_pos: int, target: int) -> bool:
    return target == array[target_pos]


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        pivot = bisect_pivot(nums)
        target_pos = bisect_target(nums, pivot, target)

        return check_target_valid(nums, target_pos, target)
