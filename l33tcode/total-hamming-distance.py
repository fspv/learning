from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = [0] * (max(nums).bit_length() if nums else 0)

        for num in nums:
            for pos in range(len(count)):
                if num & 1:
                    count[pos] += 1
                num >>= 1

        return sum(x * (len(nums) - x) for x in count)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.totalHammingDistance([]) == 0

    def test_case1(self):
        assert self.sol.totalHammingDistance([4, 14, 2]) == 6

    def test_case2(self):
        assert self.sol.totalHammingDistance([1, 10, 80, 1000, 3, 12, 0]) == 78

    def test_case3(self):
        for i in range(40):
            assert self.sol.totalHammingDistance([10 ** 9] * 10 ** 4) == 0
