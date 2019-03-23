import unittest


class Solution:
    def nextPermutation(self, nums):
        left, right = 0, len(nums) - 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                smallest = i
                for j in range(i + 1, len(nums)):
                    if nums[i - 1] < nums[j] <= nums[smallest]:
                        smallest = j

                nums[smallest], nums[i - 1] = nums[i - 1], nums[smallest]
                left, right = i, len(nums) - 1
                break

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertListEqual(self.sol.nextPermutation([]), [])

    def test_one(self):
        self.assertListEqual(self.sol.nextPermutation([1]), [1])

    def test_two_right(self):
        self.assertListEqual(self.sol.nextPermutation([1, 2]), [2, 1])

    def test_two_wrong(self):
        self.assertListEqual(self.sol.nextPermutation([2, 1]), [1, 2])

    def test_custom1(self):
        self.assertListEqual(self.sol.nextPermutation([1,2,3]), [1,3,2])

    def test_custom2(self):
        self.assertListEqual(self.sol.nextPermutation([3,2,1]), [1,2,3])

    def test_custom3(self):
        self.assertListEqual(self.sol.nextPermutation([1,1,5]), [1,5,1])

    def test_custom4(self):
        self.assertListEqual(self.sol.nextPermutation([1,3,2]), [2,1,3])

    def test_custom5(self):
        self.assertListEqual(self.sol.nextPermutation([2,3,4,5,6,7,8,1,1,5]), [2,3,4,5,6,7,8,1,5,1])

    def test_custom6(self):
        self.assertListEqual(self.sol.nextPermutation([4,2,0,2,3,2,0]), [4,2,0,3,0,2,2])

    def test_custom7(self):
        self.assertListEqual(self.sol.nextPermutation([2,3,1,3,3]), [2,3,3,1,3])


if __name__ == "__main__":
    unittest.main()
