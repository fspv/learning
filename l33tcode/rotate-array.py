from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rotate_right(array: List[int], start: int, skip: int) -> int:
            tmp = array[start]
            current = start
            count = 0

            while True:
                current = (current + skip) % len(array)
                array[current], tmp = tmp, array[current]
                count += 1

                if start == current:
                    break

            return count

        shift = k % len(nums)
        count = 0

        for start in range(shift):
            if count == len(nums):
                break

            count += rotate_right(nums, start, shift)

    def rotate_2pass(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(array: List[int], start: int, end: int) -> None:
            end -= 1

            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

        shift = (len(nums) - k) % len(nums)

        reverse(nums, 0, shift)
        reverse(nums, shift, len(nums))
        reverse(nums, 0, len(nums))
