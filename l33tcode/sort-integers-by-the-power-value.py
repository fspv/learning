class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def transform_even(num):
            return num / 2

        def transform_odd(num):
            return 3 * num + 1

        powers = []

        for num in range(lo, hi + 1):
            power = 0
            while num != 1:
                if num % 2 == 0:
                    num = transform_even(num)
                else:
                    num = transform_odd(num)
                power += 1

            powers.append(power)

        return sorted(range(lo, hi + 1), key=lambda n: (powers[n - lo], n))[k - 1]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.getKth(12, 15, 2) == 13

    def test_case2(self):
        assert self.sol.getKth(1, 1, 1) == 1

    def test_case3(self):
        assert self.sol.getKth(7, 11, 4) == 7

    def test_case4(self):
        assert self.sol.getKth(10, 20, 5) == 13

    def test_case5(self):
        assert self.sol.getKth(1, 1000, 777) == 570
