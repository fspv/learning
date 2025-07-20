class Solution:
    def _check_even_valid(self, nums, pos):
        if pos > 0 and nums[pos - 1] < nums[pos]:
            return False
        if pos < len(nums) - 1 and nums[pos + 1] < nums[pos]:
            return False
        return True

    def _check_odd_valid(self, nums, pos):
        if pos > 0 and nums[pos - 1] > nums[pos]:
            return False
        if pos < len(nums) - 1 and nums[pos + 1] > nums[pos]:
            return False
        return True

    def wiggleSort(self, nums):
        nums_sorted = sorted(nums)

        left, right = 0, len(nums_sorted) - 1

        while left <= right:
            if left == right:
                nums[left * 2] = nums_sorted[left]
            else:
                nums[left * 2] = nums_sorted[left]
                nums[left * 2 + 1] = nums_sorted[right]

            left += 1
            right -= 1


    def wiggleSortBruteForce(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        for pos in range(len(nums)):
            if pos % 2 == 0:
                if not self._check_even_valid(nums, pos):
                    for new_pos in range(pos + 1, len(nums)):
                        nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
                        if self._check_even_valid(nums, pos):
                            continue
                        else:
                            nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
            else:
                if not self._check_odd_valid(nums, pos):
                    for new_pos in range(pos + 1, len(nums)):
                        nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
                        if self._check_odd_valid(nums, pos):
                            continue
                        else:
                            nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
