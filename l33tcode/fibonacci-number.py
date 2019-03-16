import unittest


def mem_input(func):
    def wrapper(*args):
        if args[1] in args[0].mem:
            return args[0].mem[args[1]]
        else:
            args[0].mem[args[1]] = func(*args)
            return args[0].mem[args[1]]
    return wrapper


class Solution:
    mem = dict()

    @mem_input
    def fib(self, N):
        if N < 2:
            return N
        else:
            return self.fib(N - 2) + self.fib(N - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.fib(0), 0)

    def test1(self):
        self.assertEqual(self.sol.fib(1), 1)

    def test2(self):
        self.assertEqual(self.sol.fib(2), 1)

    def test3(self):
        self.assertEqual(self.sol.fib(3), 2)

    def test4(self):
        self.assertEqual(self.sol.fib(4), 3)

    def test5(self):
        self.assertEqual(self.sol.fib(5), 5)

    def test50(self):
        self.assertEqual(self.sol.fib(50), 12586269025)


if __name__ == "__main__":
    unittest.main()
