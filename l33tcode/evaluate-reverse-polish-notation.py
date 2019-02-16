import unittest

class Solution:
    def add(self, first, second):
        return first + second

    def substract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        return first / second

    def evalRPN(self, tokens: 'List[str]') -> 'int':
        operators = {
            "+": self.add,
            "-": self.substract,
            "*": self.multiply,
            "/": self.divide,
        }

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(operators[token](first, second))

        return int(stack.pop())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sum(self):
        self.assertEqual(self.sol.evalRPN(["1", "3", "+"]), 4)

    def test_multiply(self):
        self.assertEqual(self.sol.evalRPN(["2", "3", "*"]), 6)

    def test_substract(self):
        self.assertEqual(self.sol.evalRPN(["2", "3", "-"]), -1)

    def test_divide(self):
        self.assertEqual(self.sol.evalRPN(["6", "3", "/"]), 2)

    def test_complex1(self):
        self.assertEqual(self.sol.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_complex2(self):
        self.assertEqual(self.sol.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_complex3(self):
        self.assertEqual(
            self.sol.evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22
        )


if __name__ == "__main__":
    unittest.main()
