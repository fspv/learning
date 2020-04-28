class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for row in range(len(text1)):
            for col in range(len(text2)):
                dp[row + 1][col + 1] = max(
                    dp[row][col] + int(text1[row] == text2[col]),
                    dp[row + 1][col],
                    dp[row][col + 1],
                )

        return dp[-1][-1]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.longestCommonSubsequence("abcde", "ace") == 3

    def test_case2(self):
        assert self.sol.longestCommonSubsequence("abc", "abc") == 3
        assert self.sol.longestCommonSubsequence("abbc", "abc") == 3
        assert self.sol.longestCommonSubsequence("acb", "abc") == 2
        assert self.sol.longestCommonSubsequence("xabcbbcc", "abcc") == 4

    def test_case3(self):
        assert self.sol.longestCommonSubsequence("abc", "def") == 0

    def test_case4(self):
        assert (
            self.sol.longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg") == 3
        )

    def test_case5(self):
        assert (
            self.sol.longestCommonSubsequence(
                "fcvqfcnglshwpgxujwrylqzejmdubkxs", "bctsfwdelkdqzshupmrufyxklsjurevip"
            )
            == 11
        )
