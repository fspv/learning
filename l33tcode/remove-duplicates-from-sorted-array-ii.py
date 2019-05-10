class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        count = 0

        for pos in range(len(nums)):
            if count < 2 and (pos < 1 or nums[pos] == nums[pos - 1]):
                nums[length] = nums[pos]
                length += 1
                count += 1
            elif nums[pos] != nums[pos - 1]:
                nums[length] = nums[pos]
                length += 1
                count = 1

        return length
