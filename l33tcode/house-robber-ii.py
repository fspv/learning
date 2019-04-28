class Solution:
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_rec(start, end):
            if start >= end:
                dp[start] = 0
                return dp[start]

            if start in dp:
                return dp[start]

            dp[start + 2] = rob_rec(start + 2, end)
            dp[start + 3] = rob_rec(start + 3, end)

            return max(
                (dp[start + 2] + nums[start]) if start < end else 0,
                (dp[start + 3] + nums[start + 1]) if start + 1 < end else 0
            )

        dp = {}
        first = (rob_rec(0, len(nums) - 1))
        dp = {}
        second = (rob_rec(1, len(nums)))

        return max(first, second)

class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_zero(self):
        assert self.sol.rob([]) == 0

    def test_one(self):
        assert self.sol.rob([3]) == 3

    def test_custom1(self):
        assert self.sol.rob([1,2,3,1]) == 4

    def test_custom2(self):
        assert self.sol.rob([2,7,9,3,1]) == 11

    def test_custom3(self):
        assert self.sol.rob([2,1,2,1,1,2,1,2]) == 6

    def test_custom4(self):
        assert self.sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]) == 3365
