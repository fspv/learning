class Solution:
    def subarraySum(self, nums, k):
        left_right_sums = [0]
        for num in nums:
            left_right_sums.append(left_right_sums[-1] + num)

        right_left_sums = [0]
        for num in reversed(nums):
            right_left_sums.append(right_left_sums[-1] + num)

        right_left_diff_k_map = {}
        for pos, rl_sum in enumerate(right_left_sums):
            if rl_sum not in right_left_diff_k_map: 
                right_left_diff_k_map[rl_sum] = []
            right_left_diff_k_map[rl_sum].append(len(right_left_sums) - pos - 1)

        count = 0

        for pos in range(len(left_right_sums)):
            remains = left_right_sums[-1] - k - left_right_sums[pos]
            if remains in right_left_diff_k_map:
                for rl_map_pos in reversed(range(len(right_left_diff_k_map[remains]))):
                    if right_left_diff_k_map[remains][rl_map_pos] > pos:
                        count += len(right_left_diff_k_map[remains][:rl_map_pos + 1])
                        break

        return count


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty1(self):
        assert self.sol.subarraySum([], 0) == 0

    def test_empty2(self):
        assert self.sol.subarraySum([], 1) == 0

    def test_custom1(self):
        assert self.sol.subarraySum([1,1,1], 2) == 2

    def test_custom2(self):
        assert self.sol.subarraySum([1,2,1,1], 3) == 2
