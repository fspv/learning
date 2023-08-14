import random
from typing import List


def quickselect(array: List[int], k: int, left: int, right: int) -> int:
    if left >= right:
        return array[right - 1]

    pivot_ptr = random.randint(left, right - 1)
    array[right - 1], array[pivot_ptr] = array[pivot_ptr], array[right - 1]

    pivot = array[right - 1]

    partition = left

    for pos in range(left, right):
        if array[pos] <= pivot:
            array[pos], array[partition] = array[partition], array[pos]  # swap
            partition += 1

    if partition > k:
        return quickselect(array, k, left, partition - 1)
    elif partition < k:
        return quickselect(array, k, partition, right)

    return array[partition - 1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quickselect(nums, len(nums) - k + 1, 0, len(nums))


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.findKthLargest([1], 1) == 1

    def test_custom1(self):
        assert self.sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_custom2(self):
        assert self.sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
