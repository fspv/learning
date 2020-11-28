from typing import List
from functools import lru_cache


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        dp_left_right = [1] * len(nums)

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] < nums[right]:
                    dp_left_right[right] = max(
                        dp_left_right[right], dp_left_right[left] + 1
                    )

        dp_right_left = [1] * len(nums)

        for right in reversed(range(len(nums))):
            for left in reversed(range(right)):
                if nums[left] > nums[right]:
                    dp_right_left[left] = max(dp_right_left[left], dp_right_left[right] + 1)

        min_removals = len(nums) + 1

        for pos in range(1, len(nums) - 1):
            min_removals = min(
                min_removals, len(nums) - (dp_left_right[pos] + dp_right_left[pos]) + 1
            )

        return min_removals

    def minimumMountainRemovalsN2(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(prev: int, pos: int, direction: bool) -> int:
            # direction:
            # true - up
            # false - down

            if pos == len(nums):
                if not direction:
                    return 0
                else:
                    return len(nums) + 1

            min_removals = len(nums) + 1

            if direction and nums[pos] > nums[prev]:
                min_removals = min(min_removals, dp(pos, pos + 1, True))  # continue up

            if nums[pos] < nums[prev]:
                min_removals = min(min_removals, dp(pos, pos + 1, False))  # go down

            min_removals = min(
                min_removals, dp(prev, pos + 1, direction) + 1
            )  # skip this element

            return min_removals

        min_removals = float("+inf")

        for first in range(len(nums)):
            for second in range(first + 1, len(nums) - 1):
                if nums[first] < nums[second]:
                    min_removals = min(
                        min_removals, dp(second, second + 1, True) + second - 1
                    )

        return min_removals
