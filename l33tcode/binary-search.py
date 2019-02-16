import unittest

class Solution:
    def search(self, nums, target):
        if not len(nums):
            return -1

        left, right = 0, len(nums) - 1

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        if nums[left] > target:
            return -1

        if nums[right] < target:
            return -1

        while right - left > 1:
            center = int((right + left) / 2)

            if nums[center] < target:
                left = center
            elif nums[center] > target:
                right = center
            else:
                return center

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.search([], 123), -1)

    def test_one_non_matching(self):
        self.assertEqual(self.sol.search([0], 123), -1)

    def test_one_matching(self):
        self.assertEqual(self.sol.search([123], 123), 0)

    def test_out_of_boundaries_left(self):
        self.assertEqual(self.sol.search([5, 6, 7, 8, 9, 10], 2), -1)

    def test_out_of_boundaries_right(self):
        self.assertEqual(self.sol.search([5, 6, 7, 8, 9, 10], 123), -1)

    def test_not_in_array(self):
        self.assertEqual(self.sol.search([5, 6, 7, 9, 10], 8), -1)

    def test_leftmost_match(self):
        self.assertEqual(self.sol.search([5, 6, 7, 9, 10], 5), 0)

    def test_rightmost_match(self):
        self.assertEqual(self.sol.search([5, 6, 7, 9, 10], 10), 4)

    def test_central_match(self):
        self.assertEqual(self.sol.search([5, 6, 7, 9, 10], 7), 2)

    def test_match_custom1(self):
        self.assertEqual(self.sol.search([5, 6, 7, 9, 10], 6), 1)

    def test_match_custom2(self):
        self.assertEqual(self.sol.search([5, 6, 7, 9, 10], 9), 3)

if __name__ == "__main__":
    unittest.main()
