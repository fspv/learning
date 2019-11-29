from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # TODO: add solution using bisect approach
        if not k:
            return 0

        nums.append(float("+inf"))
        start, end, pos, product, result = 0, -1, 0, 1, 0
        prog_sum = lambda n: int(n * (n + 1) / 2)

        while pos < len(nums):
            if product * nums[pos] >= k:
                result += prog_sum(pos - 1 - start + 1) - prog_sum(end - start + 1)

                product = product / nums[start]
                start, end = start + 1, pos - 1
            else:
                product = product * nums[pos]
                pos += 1

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8

    def test_case2(self):
        assert self.sol.numSubarrayProductLessThanK([10, 5, 2, 6], 0) == 0
