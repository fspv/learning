import unittest


class Solution:
    def removeOuterParentheses(self, S):
        stack = []
        result = ""

        for s in S:
            if not (len(stack) == 0 or len(stack) == 1 and s == ")"):
                result += s

            if s == "(":
                stack.append("(")
            elif s == ")":
                stack.pop()

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.removeOuterParentheses(""), "")

    def test_one(self):
        self.assertEqual(self.sol.removeOuterParentheses("()"), "")

    def test_two1(self):
        self.assertEqual(self.sol.removeOuterParentheses("(())"), "()")

    def test_two2(self):
        self.assertEqual(self.sol.removeOuterParentheses("()()"), "")

    def test_custom1(self):
        self.assertEqual(self.sol.removeOuterParentheses("(()())(())"), "()()()")

    def test_custom2(self):
        self.assertEqual(self.sol.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")


if __name__ == "__main__":
    unittest.main()
