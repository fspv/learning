class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        result = nums[0] + nums[1] + nums[2]

        for pos in range(len(nums) - 2):
            left, right = pos + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[pos] + nums[left] + nums[right]

                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return cur_sum

                result = min(result, cur_sum, key=lambda x: abs(target - x))

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.threeSumClosest([], 0) == 0
        assert self.sol.threeSumClosest([1], 0) == 0
        assert self.sol.threeSumClosest([1, 2], 0) == 0

    def test_custom1(self):
        assert self.sol.threeSumClosest([1, 2, 3], 0) == 6

    def test_custom2(self):
        assert self.sol.threeSumClosest([-1, 2, 1, -4], 1) == 2

    def test_custom3(self):
        assert self.sol.threeSumClosest([0, 1, 2], 3) == 3

    def test_custom4(self):
        assert self.sol.threeSumClosest([1, 1, 1, 0], -100) == 2

    def test_custom5(self):
        assert self.sol.threeSumClosest([0, 2, 1, -3], 1) == 0
