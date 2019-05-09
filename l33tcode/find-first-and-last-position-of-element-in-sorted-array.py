class Solution:
    def searchRange(self, nums, target):
        left, right = -1, len(nums)

        while left < right - 1:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                tmp_right = right
                tmp_mid = mid
                right = mid

                while left < right - 1:
                    mid = (left + right) // 2
                    if nums[mid] < target:
                        left = mid
                    else:
                        right = mid

                result_left = left

                left = tmp_mid
                right = tmp_right

                while left < right - 1:
                    mid = (left + right) // 2
                    if nums[mid] > target:
                        right = mid
                    else:
                        left = mid

                result_right = left

                return [result_left + 1, result_right]

        return [-1, -1]


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
        assert self.sol.searchRange([5,7,7,8,8,10], 8) == [3, 4]

    def test_custom5(self):
        assert self.sol.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
