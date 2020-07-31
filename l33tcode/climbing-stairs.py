import unittest


def mem_input(func):
    def wrapper(*args):
        self = args[0]
        cur_sum = args[2] if len(args) == 3 else 0

        if self.mem is None:
            self.mem = {}

        if cur_sum in self.mem:
            return self.mem[cur_sum]
        else:
            self.mem[cur_sum] = func(*args)
            return self.mem[cur_sum]

    return wrapper


class Solution:
    mem = None

    @mem_input
    def climbStairs1(self, n, cur_sum=0):
        if cur_sum >= n:
            return 1 if cur_sum == n else 0
        else:
            return self.climbStairs(n, cur_sum + 1) + \
                   self.climbStairs(n, cur_sum + 2)

    def climbStairs(self, n: int) -> int:
        step, prev_step, prev_prev_step = 1, 1, 0

        for _ in range(n):
            step = prev_step + prev_prev_step

            prev_step, prev_prev_step = step, prev_step

        return step


class TestSolution(unittest.TestCase):
    def test0(self):
        self.sol = Solution()
        self.assertEqual(self.sol.climbStairs(0), 1)

    def test1(self):
        self.sol = Solution()
        self.assertEqual(self.sol.climbStairs(1), 1)

    def test2(self):
        self.sol = Solution()
        self.assertEqual(self.sol.climbStairs(2), 2)

    def test3(self):
        self.sol = Solution()
        self.assertEqual(self.sol.climbStairs(3), 3)

    def test5(self):
        self.sol = Solution()
        self.assertEqual(self.sol.climbStairs(5), 8)


if __name__ == "__main__":
    unittest.main()
