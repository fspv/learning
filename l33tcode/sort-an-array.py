import random
from typing import List


def quicksort(array: List[int], left: int, right: int) -> None:
    if left >= right:
        return

    pivot_ptr = random.randint(left, right - 1)
    array[right - 1], array[pivot_ptr] = array[pivot_ptr], array[right - 1]

    pivot = array[right - 1]

    partition = left

    for pos in range(left, right):
        if array[pos] <= pivot:
            array[pos], array[partition] = array[partition], array[pos]
            partition += 1

    quicksort(array, left, partition - 1)
    quicksort(array, partition, right)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quicksort(nums, 0, len(nums))

        return nums
