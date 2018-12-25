import unittest

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_1 = max(nums, key=lambda x: abs(x))
        nums.remove(num_1)
        num_2 = max(nums, key=lambda x: abs(x))
        nums.remove(num_2)

        if (num_1 < 0 and num_2 < 0) or (num_1 > 0 and num_2 > 0):
            third = max(nums)
        else:
            third = min(nums)

        return num_1 * num_2 * third


class TestSolution(unittest.TestCase):
    def test_maximum_product(self):
        solution = Solution()

        self.assertEqual(solution.maximumProduct([1, 2, 3]), 6)
        self.assertEqual(solution.maximumProduct([1, 2, 3, 4]), 24)
        self.assertEqual(solution.maximumProduct([-4, -3, -2, -1, 60]), 720)
        self.assertEqual(solution.maximumProduct([0, 2, 3]), 0)
        self.assertEqual(solution.maximumProduct([0, 0, 0]), 0)
        self.assertEqual(solution.maximumProduct([-2, -1, 0, 1, 2]), 4)
        self.assertEqual(solution.maximumProduct([-3, -2, -1]), -6)
