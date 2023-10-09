from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        first = left if nums[left] == target else -1

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        last = left - 1 if nums[left - 1] == target else -1

        return [first, last]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.searchRange([], 0) == [-1, -1]

    def test_custom2(self):
        assert self.sol.searchRange([0], 0) == [0, 0]

    def test_custom3(self):
        assert self.sol.searchRange([0, 0], 0) == [0, 1]

    def test_custom4(self):
        assert self.sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    def test_custom5(self):
        assert self.sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
