class Solution:
    def canJump(self, nums):
        dp = len(nums)

        for pos in reversed(range(len(nums))):
            if pos + nums[pos] >= dp or pos == len(nums) - 1:
                dp = pos

        return dp == 0


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.canJump([]) == True

    def test_custom1(self):
        assert self.sol.canJump([2,3,1,1,4]) == True

    def test_custom2(self):
        assert self.sol.canJump([3,2,1,0,4]) == False

    def test_custom3(self):
        assert self.sol.canJump([2, 0]) == True

    def test_custom4(self):
        assert self.sol.canJump([1, 0]) == True
