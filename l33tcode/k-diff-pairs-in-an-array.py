import unittest

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = []
        nums.sort()

        pos_new = 0

        for pos in range(len(nums)):
            pos_new = pos if pos_new < pos else pos_new # Skip values that
                                                        # certainly on less than
                                                        # k distance
            for pos2 in range(pos_new + 1, len(nums)):
                diff = nums[pos2] - nums[pos]
                if diff > k:
                    break
                elif diff == k:
                    pairs.append((nums[pos], nums[pos2]))
                    pos_new = pos2

        return len(set(pairs))


class Tests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        self.assertEqual(self.sol.findPairs([3, 1, 4, 1, 5], 2), 2)
        self.assertEqual(self.sol.findPairs([1, 2, 3, 4, 5], 1), 4)
        self.assertEqual(self.sol.findPairs([1, 3, 1, 5, 4], 0), 1)


unittest.main()
