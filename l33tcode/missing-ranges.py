class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        result = []

        for pos in range(len(nums) - 1):
            distance = nums[pos + 1] - nums[pos]
            if distance > 2:
                result.append("{}->{}".format(nums[pos] + 1, nums[pos + 1] - 1))
            elif distance == 2:
                result.append(str(nums[pos] + 1))

        return result
