import unittest

class Solution(object):
    def moveZeroesWithExtraSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zero_positions = [pos for pos in range(len(nums)) if nums[pos] == 0]
        zero_positions.append(len(nums))

        for n in range(len(zero_positions) - 1):
            for i in range(zero_positions[n] - n, zero_positions[n + 1] - n - 1):
                nums[i], nums[i + 1 + n] = nums[i + 1 + n], nums[i]

        return nums

    def moveZeroesOld(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start_zero_pos = -1

        for pos in range(len(nums)):
            if nums[pos] == 0:
                if start_zero_pos == -1:
                    start_zero_pos = pos
            elif start_zero_pos != -1:
                nums[start_zero_pos], nums[pos] = nums[pos], nums[start_zero_pos]
                start_zero_pos += 1

        return nums

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0

        for pos in range(len(nums)):
            if nums[pos] == 0:
                zeroes += 1
            else:
                nums[pos], nums[pos - zeroes] = nums[pos - zeroes], nums[pos]
