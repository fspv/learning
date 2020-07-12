class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()

        partial_max = []

        cur_max = float("-inf")

        for num in nums:
            cur_max = max(num, cur_max)
            partial_max.append(cur_max)

        result = float("+inf")

        for shift in range(4):
            result = min(
                result,
                partial_max[-1 - shift] - partial_max[3 - shift],
            )

        return result
