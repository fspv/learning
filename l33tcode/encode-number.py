class Solution:
    def encode(self, num: int) -> str:
       return bin(num + 1)[3:]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.encode(0) == ""

    def test_case2(self):
        assert self.sol.encode(1) == "0"

    def test_case3(self):
        assert self.sol.encode(2) == "1"

    def test_case4(self):
        assert self.sol.encode(3) == "00"

    def test_case5(self):
        assert self.sol.encode(4) == "01"

    def test_case6(self):
        assert self.sol.encode(5) == "10"

    def test_case7(self):
        assert self.sol.encode(6) == "11"

    def test_case8(self):
        assert self.sol.encode(7) == "000"

    def test_case9(self):
        assert self.sol.encode(23) == "1000"

    def test_case10(self):
        assert self.sol.encode(107) == "101100"
