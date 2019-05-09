class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pos1 = len(num1) - 1
        result = [0] * (len(num1) + 1)

        for pos2 in reversed(range(len(num2))):
            remains = 0
            old_result = result
            result = result[::]

            for pos1 in reversed(range(len(num1))):
                n1, n2 = int(num1[pos1]), int(num2[pos2])

                mult = n1 * n2 + remains

                remains = mult // 10
                result[len(num1) - pos1 - 1 + len(num2) - pos2 - 1] = mult % 10

            result[-1] = remains

            remains = 0

            for pos in range(len(num2) - pos2 - 1, len(old_result)):
                added = result[pos] + old_result[pos] + remains
                result[pos] = added % 10
                remains = added // 10

            result += [0]
            result[-1] = remains

        return "".join([str(r) for r in reversed(result)]).lstrip("0") or "0"


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.multiply("2", "3") == "6"

    def test_custom2(self):
        assert self.sol.multiply("123", "456") == "56088"

    def test_custom3(self):
        assert self.sol.multiply("29", "9") == "261"

    def test_custom4(self):
        assert self.sol.multiply("21", "2") == "42"

    def test_custom5(self):
        assert self.sol.multiply("0", "0") == "0"
