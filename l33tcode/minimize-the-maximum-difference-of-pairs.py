from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], pairs: int) -> int:
        nums.sort()

        def pairs_exist(max_diff: int) -> bool:
            count = 0
            pos = 1

            while pos < len(nums):
                if nums[pos] - nums[pos - 1] <= max_diff:
                    count += 1
                    pos += 1

                pos += 1

            return count >= pairs

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2

            if not pairs_exist(mid):
                left = mid + 1
            else:
                right = mid

        return left
