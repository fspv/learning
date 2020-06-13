from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums = list(reversed(sorted(nums)))

        count = [1] * len(nums)
        prev = list(range(len(nums)))

        max_count, max_seq_end = 1, 0

        for pos in range(len(nums)):
            for pos_prev in range(pos):
                if (
                    nums[pos_prev] % nums[pos] == 0
                    and count[pos] <= count[pos_prev] + 1
                ):
                    count[pos] = count[pos_prev] + 1
                    prev[pos] = pos_prev
                    if count[pos] > max_count:
                        max_count, max_seq_end = count[pos], pos

        pos = max_seq_end
        result = []
        while prev[pos] != pos:
            result.append(nums[pos])
            pos = prev[pos]

        result.append(nums[pos])

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.largestDivisibleSubset([1, 2, 3]) == [1, 2]

    def test_case2(self):
        assert self.sol.largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]
