class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        shift = 0
        nums_length = len(nums)

        while pos < nums_length:
            spos = pos - shift

            if nums[spos] == val:
                del nums[spos]
                shift += 1

            pos += 1

        return nums_length - shift


solution = Solution()

arr = []
assert solution.removeElement(arr, 123) == 0
assert arr == []

arr = [123]
assert solution.removeElement(arr, 123) == 0
assert arr == []

arr = [1]
assert solution.removeElement(arr, 123) == 1
assert arr == [1]

arr = [3, 2, 2, 3]
assert solution.removeElement(arr, 3) == 2
assert arr == [2, 2]

arr = [0, 1, 2, 2, 3, 0, 4, 2]
assert solution.removeElement(arr, 2) == 5
assert arr == [0, 1, 3, 0, 4]
