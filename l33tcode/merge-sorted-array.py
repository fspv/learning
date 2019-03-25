import unittest

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        free_ptr = m + n - 1
        ptr_last1 = m - 1
        ptr_last2 = n - 1

        while free_ptr > ptr_last1 and ptr_last2 >= 0:
            if ptr_last1 >=0 and nums1[ptr_last1] > nums2[ptr_last2]:
                nums1[free_ptr] = nums1[ptr_last1]
                ptr_last1 -= 1
            else:
                nums1[free_ptr] = nums2[ptr_last2]
                ptr_last2 -= 1

            free_ptr -= 1

        return nums1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertListEqual(self.sol.merge([], 0, [], 0), [])

    def test_one1(self):
        self.assertListEqual(self.sol.merge([2,0], 1, [1], 1), [1,2])

    def test_one2(self):
        self.assertListEqual(self.sol.merge([1,0], 1, [2], 1), [1,2])

    def test_custom1(self):
        self.assertListEqual(self.sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])


if __name__ == "__main__":
    unittest.main()
