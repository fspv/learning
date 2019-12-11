from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # TODO: solve with DP
        div = 3
        rem_map = {r: [] for r in range(1, div)}
        total = sum(nums)

        for num in nums:
            if num % div:
                rem_map[num % div].append(num)

        result = total if total % div == 0 else 0

        for rem in range(1, div):
            tmp_total = total

            for num in list(sorted(rem_map[rem]))[:div]:
                tmp_total -= num
                if tmp_total % div == 0:
                    result = max(result, tmp_total)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.maxSumDivThree([3,6,5,1,8]) == 18

    def test_case2(self):
        assert self.sol.maxSumDivThree([4]) == 0

    def test_case3(self):
        assert self.sol.maxSumDivThree([1,2,3,4,4]) == 12

    def test_case4(self):
        assert self.sol.maxSumDivThree([1,2,3]) == 6

    def test_case5(self):
        assert self.sol.maxSumDivThree([2,6,2,2,7]) == 15
