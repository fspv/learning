from typing import List
import unittest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def evaluate(string: str) -> str:
            stack: List[str] = []
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        return evaluate(s) == evaluate(t)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty1(self):
        self.assertEqual(self.sol.backspaceCompare("", ""), True)

    def test_empty2(self):
        self.assertEqual(self.sol.backspaceCompare("", "a#"), True)

    def test_empty3(self):
        self.assertEqual(self.sol.backspaceCompare("a#", "a#"), True)

    def test_empty4(self):
        self.assertEqual(self.sol.backspaceCompare("a#", ""), True)

    def test_empty5(self):
        self.assertEqual(self.sol.backspaceCompare("a#", "a"), False)

    def test_empty6(self):
        self.assertEqual(self.sol.backspaceCompare("ab##", "c#d#"), True)

    def test_custom1(self):
        self.assertEqual(self.sol.backspaceCompare("a##c", "#a#c"), True)

    def test_custom2(self):
        self.assertEqual(self.sol.backspaceCompare("a#c", "b"), False)

    def test_custom3(self):
        self.assertEqual(
            self.sol.backspaceCompare("abcdef#gh", "abcdef#f#f#f#ghvg##"), True
        )

    def test_custom4(self):
        self.assertEqual(self.sol.backspaceCompare("bxj##tw", "bxj###tw"), False)

    def test_custom5(self):
        self.assertEqual(self.sol.backspaceCompare("bbbextm", "bbb#extm"), False)


if __name__ == "__main__":
    unittest.main()
