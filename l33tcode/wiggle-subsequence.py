from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        dp_up = [0] * len(nums)
        dp_up[-1] = 1
        if nums[-2] < nums[-1]:
            dp_up[-2] = 2

        dp_down = [0] * len(nums)
        dp_down[-1] = 1
        if nums[-2] > nums[-1]:
            dp_down[-2] = 2

        for pos in reversed(range(len(nums))):
            for next_pos in range(pos + 1, len(nums)):
                if nums[pos] < nums[next_pos]:
                    dp_up[pos] = max(dp_down[next_pos] + 1, dp_up[pos])
                if nums[pos] > nums[next_pos]:
                    dp_down[pos] = max(dp_up[next_pos] + 1, dp_down[pos])

        return max(max(dp_up), max(dp_down))
