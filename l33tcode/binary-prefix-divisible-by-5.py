import unittest

class Solution:
    def prefixesDivBy5(self, A):
        result = [False] * len(A)
        cur = 0

        for pos in range(len(A)):
            cur = cur * 2 + A[pos]

            if (cur % 5) == 0:
                result[pos] = True

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertListEqual(self.sol.prefixesDivBy5([]), [])

    def test_one1(self):
        self.assertListEqual(self.sol.prefixesDivBy5([0]), [True])

    def test_one2(self):
        self.assertListEqual(self.sol.prefixesDivBy5([1]), [False])

    def test_custom1(self):
        self.assertListEqual(self.sol.prefixesDivBy5([0,1,1]), [True,False,False])

    def test_custom2(self):
        self.assertListEqual(self.sol.prefixesDivBy5([1,1,1]), [False,False,False])

    def test_custom3(self):
        self.assertListEqual(self.sol.prefixesDivBy5([0,1,1,1,1,1]), [True,False,False,False,True,False])

    def test_custom4(self):
        self.assertListEqual(self.sol.prefixesDivBy5([1,1,1,0,1]), [False,False,False,False,False])

    def test_custom5(self):
        self.assertListEqual(self.sol.prefixesDivBy5([1,1,0,0,0,1,0,0,1]), [False,False,False,False,False,False,False,False,False])


if __name__ == "__main__":
    unittest.main()
