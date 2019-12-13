from typing import List


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def gen_number(partial):
            result = []

            for pos in range(len(partial) + 1):
                left, right = partial[:pos], partial[pos:]
                if left and not (left.startswith("0") and left != "0"):
                    if right:
                        if not right.endswith("0"):
                            result.append(f"{left}.{right}")
                    else:
                        result.append(left)

            return result

        def split(pivot):
            result = []

            for left in gen_number(S[:pivot]):
                for right in gen_number(S[pivot:]):
                    result.append("(" + left + ", " + right + ")")

            return result

        result = []

        S = S[1:-1]
        for pos in range(len(S)):
            result += split(pos)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert list(sorted(self.sol.ambiguousCoordinates("(123)"))) == list(sorted(["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]))

    def test_case2(self):
        assert list(sorted(self.sol.ambiguousCoordinates("(00011)"))) == list(sorted(["(0.001, 1)", "(0, 0.011)"]))

    def test_case3(self):
        assert list(sorted(self.sol.ambiguousCoordinates("(0123)"))) == list(sorted(["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]))

    def test_case4(self):
        assert list(sorted(self.sol.ambiguousCoordinates("(100)"))) == list(sorted(["(10, 0)"]))
