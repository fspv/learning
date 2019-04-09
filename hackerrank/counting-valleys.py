def countingValleys(n, s):
    height = 0
    result = 0

    for i in range(n):
        height += -1 if s[i] == "D" else 1
        result += 1 if s[i] == "U" and height == 0 else 0

    return result


class TestCountingValleys:
    def test_custom1(self):
        assert countingValleys(2, "DU") == 1

    def test_custom2(self):
        assert countingValleys(2, "DD") == 0

    def test_custom3(self):
        assert countingValleys(8, "UDDDUDUU") == 1

    def test_custom4(self):
        assert countingValleys(8, "DDDDDDDD") == 0

    def test_custom5(self):
        assert countingValleys(8, "DDDDUUUU") == 1

    def test_custom6(self):
        assert countingValleys(8, "DDDDDUUU") == 0
