from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for pos in range(1, len(nums)):
            nums[pos] += max(nums[pos - 1], 0)

        return max(nums) if nums else 0

    def maxSubArrayDivideAndConquer(self, nums: list[int]) -> int:
        def dfs(left: int, right: int, sums: list[int]) -> tuple[int, int, int]:
            if left == right:
                return float("+inf"), float("-inf"), float("-inf") # type: ignore
            if right - left == 1:
                return sums[left], sums[left], sums[left]

            middle = (left + right) // 2

            min_left, max_left, max_sum_left = dfs(left, middle, sums)
            min_right, max_right, max_sum_right = dfs(middle, right, sums)

            return (
                min(min_left, min_right),
                max(max_left, max_right),
                max(max_sum_left, max_sum_right, max_right - min_left),
            )

        return dfs(0, len(nums), list(accumulate(nums)))[2]

    def maxSubArray_O_n(self, nums: list[int]) -> int:
        result = float("-inf")
        min_sum_so_far = 0

        for sum_so_far in accumulate(nums):
            result = max(result, sum_so_far - min_sum_so_far)
            min_sum_so_far = min(min_sum_so_far, sum_so_far)

        return result # type: ignore


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
