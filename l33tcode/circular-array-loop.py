import unittest

# TODO: Create solution with O(1) extra space

class Solution:
    def circularArrayLoop(self, nums):
        for start in range(len(nums)):
            visited = [None] * len(nums)

            prev_pos = None
            pos = start

            while not visited[pos] and nums[start] * nums[pos] > 0:
                visited[pos] = True
                prev_pos = pos
                pos += nums[pos]
                pos = pos % len(nums) if pos % len(nums) >= 0 else len(nums) - abs(pos) % len(nums)

            if visited[pos] and pos != prev_pos and nums[start] * nums[pos] > 0:
                return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertFalse(self.sol.circularArrayLoop([1]))

    def test_2(self):
        self.assertTrue(self.sol.circularArrayLoop([1,1]))

    def test_3(self):
        self.assertTrue(self.sol.circularArrayLoop([2,-1,1,2,2]))

    def test_4(self):
        self.assertFalse(self.sol.circularArrayLoop([-1,2]))

    def test_5(self):
        self.assertFalse(self.sol.circularArrayLoop([-2,1,-1,-2,-2]))

    def test_6(self):
        self.assertFalse(self.sol.circularArrayLoop([-1]))

    def test_7(self):
        self.assertFalse(self.sol.circularArrayLoop([-2]))

    def test_8(self):
        self.assertFalse(self.sol.circularArrayLoop([-1,-2,-3,-4,-5]))


if __name__ == "__main__":
    unittest.main()
