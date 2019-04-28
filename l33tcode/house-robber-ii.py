class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = dict()

        def rob_rec(start, end):
            if start >= end:
                dp[(start, end)] = 0
                return dp[(start, end)]

            if (start, end) in dp:
                return dp[(start, end)]

            dp[(start + 2, end)] = rob_rec(start + 2, end)
            dp[(start + 3, end)] = rob_rec(start + 3, end)

            return max(
                (dp[(start + 2, end)] + nums[start]) if start < end else 0,
                (dp[(start + 3, end)] + nums[start + 1]) if start + 1 < end else 0
            )

        return max(
            (rob_rec(2, len(nums) - 1) + nums[0]) if len(nums) > 0 else 0,
            (rob_rec(3, len(nums)) + nums[1]) if len(nums) > 1 else 0,
            (rob_rec(4, len(nums)) + nums[2]) if len(nums) > 2 else 0,
        )
