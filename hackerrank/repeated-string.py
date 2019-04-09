def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:(n % len(s))].count("a")


class TestRepeatedString:
    def test_one1(self):
        assert repeatedString("a", 1000000000000) == 1000000000000

    def test_one2(self):
        assert repeatedString("b", 1000000000000) == 0

    def test_custom1(self):
        assert repeatedString("aba", 10) == 7
