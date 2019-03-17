import unittest


class Solution:
    def bitwiseComplement(self, N):
        if N == 0:
            return 1

        bin_string = '{0:08b}'.format(N)[-N.bit_length():]

        bin_string_compl = ""

        for sym in bin_string:
            bin_string_compl += "0" if sym == "1" else "1"

        return int(bin_string_compl, 2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.bitwiseComplement(0), 1)

    def test1(self):
        self.assertEqual(self.sol.bitwiseComplement(1), 0)

    def test2(self):
        self.assertEqual(self.sol.bitwiseComplement(2), 1)

    def test5(self):
        self.assertEqual(self.sol.bitwiseComplement(5), 2)

    def test7(self):
        self.assertEqual(self.sol.bitwiseComplement(7), 0)

    def test10(self):
        self.assertEqual(self.sol.bitwiseComplement(10), 5)

    def test1000(self):
        self.assertEqual(self.sol.bitwiseComplement(1000), 23)


if __name__ == "__main__":
    unittest.main()
