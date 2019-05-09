class Solution:
    def fourSum(self, nums, target):
        nums.sort()

        result = set()

        for pos1 in range(len(nums) - 3):
            for pos2 in range(pos1 + 1, len(nums) - 2):
                two_sum = nums[pos1] + nums[pos2]
                left, right = pos2 + 1, len(nums) - 1

                while left < right:
                    cur_sum = nums[left] + nums[right] + two_sum
                    if cur_sum < target:
                        left += 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        result.add(
                            (nums[pos1], nums[pos2], nums[left], nums[right])
                        )
                        left += 1
                        right -= 1

        return [list(r) for r in result]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.fourSum([], 0) == []

    def test_custom1(self):
        assert sorted(self.sol.fourSum([1, 0, -1, 0, -2, 2], 0)) == sorted([
          [-1, 0, 0, 1],
          [-2, -1, 1, 2],
          [-2, 0, 0, 2]
        ])
