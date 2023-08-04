import unittest
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for pos in range(len(s)):
            for word in wordDict:
                if (
                    pos >= len(word) - 1
                    and dp[pos - len(word) + 1]
                    and s[pos - len(word) + 1 : pos + 1] == word
                ):
                    dp[pos + 1] = True

        return dp[len(s)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one1(self):
        self.assertEqual(self.sol.wordBreak("a", ["a", "b"]), True)

    def test_one2(self):
        self.assertEqual(self.sol.wordBreak("a", ["c", "b"]), False)

    def test_custom1(self):
        self.assertEqual(self.sol.wordBreak("leetcode", ["leet", "code"]), True)

    def test_custom2(self):
        self.assertEqual(self.sol.wordBreak("applepenapple", ["apple", "pen"]), True)

    def test_custom3(self):
        self.assertEqual(
            self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]),
            False,
        )

    def test_custom4(self):
        self.assertEqual(
            self.sol.wordBreak(
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                [
                    "a",
                    "aa",
                    "aaa",
                    "aaaa",
                    "aaaaa",
                    "aaaaaa",
                    "aaaaaaa",
                    "aaaaaaaa",
                    "aaaaaaaaa",
                    "aaaaaaaaaa",
                ],
            ),
            False,
        )

    def test_custom5(self):
        self.assertEqual(self.sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]), True)


if __name__ == "__main__":
    unittest.main()
