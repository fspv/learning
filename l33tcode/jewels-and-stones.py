import unittest

class Solution:
    def numJewelsInStones1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        counter = 0

        jewel_map = {k: None for k in J}

        for s_i in S:
            if s_i in jewel_map:
                counter += 1

        return counter

    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return len([s for s in S if s in jewels])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.numJewelsInStones("", ""), 0)
        self.assertEqual(self.solution.numJewelsInStones("", "abc"), 0)
        self.assertEqual(self.solution.numJewelsInStones("abc", ""), 0)
        self.assertEqual(self.solution.numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(self.solution.numJewelsInStones("z", "ZZ"), 0)
        self.assertEqual(self.solution.numJewelsInStones("z", "zz"), 2)

if __name__ == "__main__":
    unittest.main()
