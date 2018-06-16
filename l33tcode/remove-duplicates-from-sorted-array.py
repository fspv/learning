class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        shift = 0
        pos = 0
        num_length = len(nums)

        while pos < num_length:
            spos = pos - shift
            if spos > 0 and nums[spos - 1] == nums[spos]:
                del nums[spos]
                shift += 1
            pos += 1

        return num_length - shift

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        inplace_update_pos = 0
        current_pos = 0

        for num in nums:
            if num != nums[inplace_update_pos]:
                if (inplace_update_pos + 1) != current_pos:
                    nums[inplace_update_pos + 1] = num
                inplace_update_pos += 1

            current_pos += 1

        for i in range(len(nums) - (inplace_update_pos + 1)):
            nums.pop()

        return (inplace_update_pos + 1) if current_pos > 0 else 0

solution = Solution()
arr = []
assert solution.removeDuplicates(arr) == 0
assert arr == []

arr = [0]
assert solution.removeDuplicates(arr) == 1
assert arr == [0]

arr = [1,1,2]
assert solution.removeDuplicates(arr) == 2
assert arr == [1,2]

arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert solution.removeDuplicates(arr) == 5
assert arr == [0, 1, 2, 3, 4]
