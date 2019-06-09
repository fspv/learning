class Solution:
    def findOcurrences(self, text, first, second):
        result = []

        words = text.split(" ")

        if len(words) < 3:
            return result

        for pos in range(2, len(words)):
            if words[pos - 2] == first and words[pos - 1] == second:
                result.append(words[pos])

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.findOcurrences("", "", "") == []
        assert self.sol.findOcurrences("", "a", "a") == []

    def test_custom1(self):
        assert self.sol.findOcurrences("alice is a good girl she is a good student", "a", "good") == ["girl", "student"]
        assert self.sol.findOcurrences("alice is a good girl she is a good stUdent", "a", "good") == ["girl", "stUdent"]

    def test_custom2(self):
        assert self.sol.findOcurrences("we will we will rock you", "we", "will") == ["we", "rock"]

    def test_custom3(self):
        assert self.sol.findOcurrences("a a a a a A a", "a", "a") == ["a", "a", "a", "A"]
