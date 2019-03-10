import unittest
from collections import deque


class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1

        queue = deque()
        pos = N
        tmp = deque()

        while pos > 0:
            tmp.append(pos)

            for op in ["*", "/", "+", "-"]:
                if pos - 1 == 0:
                    queue += tmp
                    pos -= 1
                    break

                if op in ["/", "*"]:
                    tmp.appendleft(op)
                    tmp.append(pos - 1)
                elif op  == "+":
                    queue.appendleft(op)
                    queue += tmp
                    tmp = deque()
                    queue.append(pos - 1)
                else:
                    queue.appendleft(op)

                pos -= 1

        stack = [queue.popleft(), queue.popleft(), queue.popleft()]

        while len(stack) > 1:
            if stack[-1] not in ["*", "/", "+", "-"] and \
               stack[-2] not in ["*", "/", "+", "-"]:
                right = stack.pop()
                left = stack.pop()
                op = stack.pop()
                if op == "-":
                    stack.append(left - right)
                elif op == "+":
                    stack.append(left + right)
                elif op == "/":
                    stack.append(int(left / right))
                elif op == "*":
                    stack.append(left * right)
            else:
                stack.append(queue.popleft())

        return int(stack[-1])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one(self):
        self.assertEqual(self.sol.clumsy(1), 1)

    def test_four(self):
        self.assertEqual(self.sol.clumsy(4), 7)

    def test_10(self):
        self.assertEqual(self.sol.clumsy(10), 12)


if __name__ == "__main__":
    unittest.main()
