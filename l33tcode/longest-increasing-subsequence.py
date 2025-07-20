class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 2:
            return len(nums)

        dp = [1] * len(nums)

        for pos in range(1, len(nums)):
            for prev_pos in range(0, pos):
                if nums[prev_pos] < nums[pos] and dp[prev_pos] + 1 > dp[pos]:
                    dp[pos] = dp[prev_pos] + 1

        return max(dp)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.lengthOfLIS([]) == 0

    def test_one(self):
        assert self.sol.lengthOfLIS([2]) == 1

    def test_custom1(self):
        assert self.sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_custom2(self):
        assert self.sol.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
