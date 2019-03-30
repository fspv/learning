import unittest

class Solution:
    def productExceptSelf(self, nums):
        forward = [0] * len(nums)
        reverse = [0] * len(nums)
        result = [0] * len(nums)

        for f in range(len(nums)):
            forward[f] = (forward[f - 1] if f > 0 else 1) * nums[f]

        for r in range(len(nums) - 1, -1, -1):
            reverse[r] = (reverse[r + 1] if r < len(nums) - 1 else 1) * nums[r]

        for n in range(len(nums)):
            prev_res = forward[n - 1] if n > 0 else 1
            next_res = reverse[n + 1] if n < len(nums) - 1 else 1
            result[n] = prev_res * next_res

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertListEqual(self.sol.productExceptSelf([]), [])

    def test_one(self):
        self.assertListEqual(self.sol.productExceptSelf([1]), [1])

    def test_custom1(self):
        self.assertListEqual(self.sol.productExceptSelf([1,2,3,4]), [24,12,8,6])


if __name__ == "__main__":
    unittest.main()
