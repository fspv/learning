from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        chars = []
        count = Counter()

        for c in s:
            if count[c] == 0:
                chars.append(c)
            count[c] += 1

        chars.sort()

        result_arr = []

        direction = True

        while any([count[c] > 0 for c in chars]):
            for c in chars if direction else reversed(chars):
                if count[c] > 0:
                    result_arr.append(c)
                    count[c] -= 1

            direction = not direction

        return "".join(result_arr)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.sortString("") == ""

    def test_case1(self):
        assert self.sol.sortString("aaaabbbbcccc") == "abccbaabccba"

    def test_case2(self):
        assert self.sol.sortString("rat") == "art"

    def test_case3(self):
        assert self.sol.sortString("leetcode") == "cdelotee"

    def test_case4(self):
        assert self.sol.sortString("ggggggg") == "ggggggg"

    def test_case4(self):
        assert self.sol.sortString("spo") == "ops"
