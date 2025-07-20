import unittest

class Solution:
    def maxScoreSightseeingPair(self, A):
        left = [elem + num for num, elem in enumerate(A)]
        right = [elem - num for num, elem in enumerate(A)]
        right_maximums = []

        max_so_far = right[-1]
        for r in range(len(right) - 1, 0, -1):
            if max_so_far < right[r]:
                max_so_far = right[r]

            right_maximums.append(max_so_far)

        best_pair = 0

        for l in range(len(left) - 1):
            new_best_pair = left[l] + right_maximums.pop()
            best_pair = new_best_pair if new_best_pair > best_pair else best_pair

        return best_pair


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.maxScoreSightseeingPair([1, 1]), 1)

    def test_2(self):
        self.assertEqual(self.sol.maxScoreSightseeingPair([8,1,5,2,6]), 11)


if __name__ == "__main__":
    unittest.main()
