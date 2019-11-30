class Solution:
    def toHexspeak(self, num: str) -> str:
        num_hex = list(map(lambda x: x.upper(), list(hex(int(num))[2:])))

        error = set(map(str, list(range(2, 10))))

        for pos in range(len(num_hex)):
            if num_hex[pos] in error:
                return "ERROR"
            elif num_hex[pos] in ["0", "1"]:
                num_hex[pos] = "O" if num_hex[pos] == "0" else "I"

        return "".join(num_hex)



class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.toHexspeak("257") == "IOI"

    def test_case2(self):
        assert self.sol.toHexspeak("3") == "ERROR"

    def test_case3(self):
        assert self.sol.toHexspeak("1") == "I"

    def test_case4(self):
        assert self.sol.toHexspeak("10") == "A"

    def test_case5(self):
        assert self.sol.toHexspeak("16") == "IO"
