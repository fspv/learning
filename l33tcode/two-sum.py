class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        for i, num in enumerate(nums): # This is O(n)
            second = target - num # This is O(1)
            if second in nums_hash: # This is O(1)
                return [i, nums_hash[second]]
            else:
                nums_hash[num] = i # This is O(1)
