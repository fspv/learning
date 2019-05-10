class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1

        for pos in range(len(nums)):
            if pos > right:
                break

            while (nums[pos] == 0 and left < pos) or \
                  (nums[pos] == 2 and right > pos):
                if nums[pos] == 0 and left < pos:
                    nums[pos], nums[left] = nums[left], nums[pos]
                    left += 1

                if nums[pos] == 2 and right > pos:
                    nums[pos], nums[right] = nums[right], nums[pos]
                    right -= 1
