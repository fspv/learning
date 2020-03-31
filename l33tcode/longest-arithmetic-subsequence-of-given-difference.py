from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)
        num_pos_map = {}

        for pos in range(len(arr)):
            pos_prev = num_pos_map.get(arr[pos] - difference)
            if pos_prev is not None:
                dp[pos] = max(dp[pos], dp[pos_prev] + 1)
            num_pos_map[arr[pos]] = pos

        return max(dp)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_single_element(self):
        assert self.sol.longestSubsequence([1], 1) == 1
        assert self.sol.longestSubsequence([1], 0) == 1

    def test_case1(self):
        assert self.sol.longestSubsequence([1, 2, 3, 4], 1) == 4

    def test_case2(self):
        assert self.sol.longestSubsequence([1, 3, 5, 7], 1) == 1

    def test_case3(self):
        assert self.sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
