import unittest
from bisect import bisect
from typing import List, Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        MOD = 60
        modulos: Counter[int] = Counter(map(lambda x: x % MOD, time))

        pairs = 0

        for modulo in map(lambda x: x % MOD, time):
            modulos[modulo] -= 1
            pairs += modulos[(60 - modulo) % MOD]
            modulos[modulo] += 1

        return pairs // 2

    def numPairsDivisibleBy60Slow(self, time):
        result = 0

        time_new = time.copy()

        mem = {}

        for pos in range(len(time)):
            time_new[pos] = time[pos] % 60
            if time_new[pos] in mem:
                mem[time_new[pos]].append(pos)
            else:
                mem[time_new[pos]] = [pos]

        time = time_new

        for i in range(len(time)):
            compl = 60 - time[i]
            if compl == 60:
                compl = 0
            if compl in mem:
                start = bisect(mem[compl], i)
                for j in mem[compl][start:]:
                    result += 1

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([]), 0)

    def test_one1(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([1]), 0)

    def test_one2(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([60]), 0)

    def test_two_div(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([59, 61]), 1)

    def test_two_non_div(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([59, 60]), 0)

    def test_custom1(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([30,20,150,100,40]), 3)

    def test_custom2(self):
        self.assertEqual(self.sol.numPairsDivisibleBy60([60,60,60]), 3)


if __name__ == "__main__":
    unittest.main()
