class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for pos in range(len(s)):
            for left_offset in [1, 2]:
                right_offset = 0
                while pos - left_offset >= 0 and \
                      pos + right_offset < len(s) and \
                      s[pos - left_offset] == s[pos + right_offset]:
                    left_offset += 1
                    right_offset += 1
                    count += 1

        return count + len(s)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.countSubstrings("abc") == 3

    def test_custom2(self):
        assert self.sol.countSubstrings("aaa") == 6

    def test_custom3(self):
        assert self.sol.countSubstrings("abccbaabccba") == 24
