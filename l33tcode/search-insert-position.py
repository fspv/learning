class Solution(object):
    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

	for n, num in enumerate(nums):
            if num >= target:
                return n

        return len(nums)

    def binary_search(self, array, left, right, search):
        if array[left] < search and search < array[right]:
            if (right - left) == 1:
                return right
            middle_pos = left + (right - left) / 2
            middle = array[middle_pos]
            if search < middle:
                left_new = left
                right_new = middle_pos
            elif search > middle:
                left_new = middle_pos
                right_new = right
            else:
                return middle_pos
            return self.binary_search(array, left_new, right_new, search)
        else:
            if search <= array[left]:
                return left
            if search == array[right]:
                return right
            elif search > array[right]:
                return right + 1

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) > 0:
            return self.binary_search(nums, 0, len(nums) - 1, target)
        else:
            return 0



solution = Solution()

assert solution.searchInsert([1,3,5,6], 5) == 2
assert solution.searchInsert([1,3,5,6], 2) == 1
assert solution.searchInsert([1,3,5,6], 7) == 4
assert solution.searchInsert([1,3,5,6], 0) == 0
assert solution.searchInsert([], 123) == 0
assert solution.searchInsert([0], 1) == 1
assert solution.searchInsert([0], 0) == 0
assert solution.searchInsert([1, 2, 3], 2) == 1
