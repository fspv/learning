import unittest

class Solution:
    def canThreePartsEqualSum(self, A):
        left_sums = dict()
        left_prev_sum = 0

        for l in range(len(A) - 2):
            left_prev_sum += A[l]

            if not left_prev_sum in left_sums:
                left_sums[left_prev_sum] = []

            left_sums[left_prev_sum].append(l)

        whole_sum = left_prev_sum + sum(A[-2:])

        right_prev_sum = 0
        for r in range(len(A) - 1, 1, -1):
            right_prev_sum += A[r]

            if right_prev_sum in left_sums:
                if (whole_sum - right_prev_sum * 2) == right_prev_sum:
                    for l in left_sums[right_prev_sum]:
                        if r - l > 1:
                            return True

        return False

    def canThreePartsEqualSumBruteForce(self, A):
        left = 0
        middle = 0
        right = sum(A)

        for i in range(0, len(A) - 1):
            left += A[i]
            right -= A[i]
            mem_right = right
            middle = 0
            for j in range(i + 1, len(A)):
                middle += A[j]
                right -= A[j]
                if left == right == middle:
                    return True
            right = mem_right

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_min(self):
        self.assertTrue(self.sol.canThreePartsEqualSum([1,1,1]))

    def test_min2(self):
        self.assertFalse(self.sol.canThreePartsEqualSum([1,2,1]))

    def test_1(self):
        self.assertTrue(self.sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))

    def test_2(self):
        self.assertFalse(self.sol.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))

    def test_3(self):
        self.assertTrue(self.sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))


if __name__ == "__main__":
    unittest.main()
