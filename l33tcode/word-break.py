import unittest


class Solution:
    dp = {}

    def check_segmentable(self, s, word_len_dict, word_len_list, end_pos):
        if end_pos == -1:
            return True

        for word_len in word_len_list:
            if end_pos - word_len + 1 < 0:
                break
            if s[end_pos - word_len + 1:end_pos + 1] in word_len_dict[word_len]:
                if end_pos - word_len in self.dp:
                    return self.dp[end_pos - word_len]

                if self.check_segmentable(
                    s, word_len_dict, word_len_list, end_pos - word_len
                ):
                    return True

                self.dp[end_pos - word_len] = False

        return False

    def wordBreak(self, s, wordDict):
        word_len_dict = {}
        for word in wordDict:
            if len(word) not in word_len_dict:
                word_len_dict[len(word)] = set()
            word_len_dict[len(word)].add(word)

        word_len_list = sorted(word_len_dict.keys())

        return self.check_segmentable(
            s, word_len_dict, word_len_list, len(s) - 1
        )


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
        self.assertEqual(self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)

    def test_custom4(self):
        self.assertEqual(self.sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False)

    def test_custom5(self):
        self.assertEqual(self.sol.wordBreak("aaaaaaa", ["aaaa","aaa"]), True)


if __name__ == "__main__":
    unittest.main()
