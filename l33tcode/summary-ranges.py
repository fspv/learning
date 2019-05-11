class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left, right = 0, 0

        result = []

        for pos in range(1, len(nums) + 1):
            if pos < len(nums) and nums[pos] - nums[pos - 1] < 2:
                right += 1
            else:
                if left == right:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[right]))
                left = right = right + 1

        return result
