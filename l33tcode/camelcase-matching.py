import unittest


class Solution:
    def check(self, query, pattern):
        pattern_pos = 0

        for q in query:
            if pattern_pos < len(pattern) and q == pattern[pattern_pos]:
                pattern_pos += 1
            else:
                if q.upper() == q:
                    return False

        return pattern_pos == len(pattern)

    def camelMatch(self, queries, pattern):
        result = []

        for query in queries:
            result.append(self.check(query, pattern))

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty1(self):
        self.assertListEqual(self.sol.camelMatch([], ""), [])

    def test_empty2(self):
        self.assertListEqual(self.sol.camelMatch([], "FB"), [])

    def test_custom1(self):
        self.assertListEqual(self.sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"), [True,False,True,True,False])

    def test_custom2(self):
        self.assertListEqual(self.sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"), [True,False,True,False,False])

    def test_custom3(self):
        self.assertListEqual(self.sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack","FooBarTestT"], "FoBaT"), [False,True,False,False,False,False])

    def test_custom4(self):
        self.assertListEqual(self.sol.camelMatch(["kqshppmjgjfB","mkqsthpypmgB","kqshppmtgttB","lklqsphppmgB","kqesshppwmgB","kqshpzlcpmgB","kqsyhppmhfgB"], "kqshppmgB"), [True,True,True,True,True,True,True])


if __name__ == "__main__":
    unittest.main()
