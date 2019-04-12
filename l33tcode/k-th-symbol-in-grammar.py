class SolutionBruteForce:
    def kthGrammar(self, N: int, K: int) -> int:
        def nth_level(prev_row, levels):
            if levels == 0:
                return prev_row

            row = []
            for val in prev_row:
                if val == 0:
                    row += [0, 1]
                else:
                    row += [1, 0]

            return nth_level(row, levels - 1)

        return nth_level([0], N - 1)[K - 1]


class SolutionBruteForce2:
    # Time ok, but memory error
    def kthGrammar(self, N: int, K: int) -> int:
        def nth_level(row, levels):
            if levels == 0:
                return row

            return nth_level(row + row[len(row) // 2:] + row[:len(row) // 2], levels - 1)

        if N == 1:
            return 0

        return int(nth_level("01", N - 2)[K - 1])


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def nth_level(level, pos):
            return (pos + nth_level(level - 1, pos // 2)) % 2 if level > 0 else 0

        return nth_level(N - 1, K - 1)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.kthGrammar(1, 1) == 0

    def test_custom1(self):
        assert self.sol.kthGrammar(2, 1) == 0

    def test_custom2(self):
        assert self.sol.kthGrammar(2, 2) == 1

    def test_custom3(self):
        assert self.sol.kthGrammar(4, 5) == 1

    def test_custom3(self):
        assert self.sol.kthGrammar(5, 13) == 0

    def test_custom4(self):
        assert self.sol.kthGrammar(30, 434991989) == 0
