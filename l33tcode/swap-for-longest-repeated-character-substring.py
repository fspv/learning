from collections import defaultdict, Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        dp = defaultdict(lambda: (0, -1, -1))
        counter = Counter(text)
        result = 1

        for pos in range(len(text)):
            count, last_seen, last_swap = dp[text[pos]]

            if pos - last_seen == 1:
                count += 1
            elif pos - last_seen == 2:
                count = pos - last_swap
                last_swap = pos - 1
            else:
                count = 1
                last_swap = pos - 1

            last_seen = pos

            dp[text[pos]] = (count, last_seen, last_swap)

            add = 0 if count > pos - last_swap else 1

            result = max(min(count + add, counter[text[pos]]), result)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case0(self):
        assert self.sol.maxRepOpt1("a") == 1

    def test_case1(self):
        assert self.sol.maxRepOpt1("ababa") == 3

    def test_case2(self):
        assert self.sol.maxRepOpt1("aaabaaa") == 6

    def test_case3(self):
        assert self.sol.maxRepOpt1("aaabbaaa") == 4

    def test_case4(self):
        assert self.sol.maxRepOpt1("aaaaa") == 5

    def test_case5(self):
        assert self.sol.maxRepOpt1("abcdef") == 1

    def test_case6(self):
        assert self.sol.maxRepOpt1("aabaaabaaaba") == 7
