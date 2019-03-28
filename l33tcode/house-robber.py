import unittest

class Solution:
    memo = None

    def rob(self, nums, pos=0, robbed=0):
        if self.memo is None:
            self.memo = {}

        if pos >= len(nums):
            return 0

        if pos not in self.memo:
            self.memo[pos] = max(
                self.rob(nums, pos + 2) + nums[pos],
                self.rob(nums, pos + 1),
            )

        return self.memo[pos]

    def robBruteForce(self, nums, robbed=0, not_visited=None):
        if not_visited is None:
            not_visited = set(range(len(nums)))

        max_robbed = robbed

        for nv in not_visited:
            not_visited_new = not_visited.copy()
            not_visited_new.remove(nv)
            if nv - 1 in not_visited_new:
                not_visited_new.remove(nv - 1)
            if nv + 1 in not_visited_new:
                not_visited_new.remove(nv + 1)

            res = self.rob(nums, robbed + nums[nv], not_visited_new)
            max_robbed = res if max_robbed < res else max_robbed

        return max_robbed


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(self.sol.rob([]), 0)

    def test_one(self):
        self.assertEqual(self.sol.rob([3]), 3)

    def test_custom1(self):
        self.assertEqual(self.sol.rob([1,2,3,1]), 4)

    def test_custom2(self):
        self.assertEqual(self.sol.rob([2,7,9,3,1]), 12)

    def test_custom3(self):
        self.assertEqual(self.sol.rob([2,1,2,1,1,2,1,2]), 8)

    def test_custom4(self):
        self.assertEqual(self.sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]), 3365)


if __name__ == "__main__":
    unittest.main()
