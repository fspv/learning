# TODO: understand the algorithm better
# TODO: add divide and conquer solution

class Solution:
    def maxSubArray(self, nums):
        for pos in range(1, len(nums)):
            nums[pos] += max(nums[pos - 1], 0)

        return max(nums) if nums else 0


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.maxSubArray([]) == 0

    def test_one(self):
        assert self.sol.maxSubArray([1]) == 1

    def test_two1(self):
        assert self.sol.maxSubArray([1, 1]) == 2

    def test_two2(self):
        assert self.sol.maxSubArray([1, -1]) == 1

    def test_two3(self):
        assert self.sol.maxSubArray([-1, 1]) == 1

    def test_two4(self):
        assert self.sol.maxSubArray([0, 1]) == 1

    def test_custom1(self):
        assert self.sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
