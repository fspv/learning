from nesting_depth import solution


class TestSolution:
    def test_solution1(self):
        assert solution("") == ""

    def test_solution2(self):
        assert solution("0000") == "0000"

    def test_solution3(self):
        assert solution("101") == "(1)0(1)"

    def test_solution4(self):
        assert solution("111000") == "(111)000"

    def test_solution5(self):
        assert solution("1") == "(1)"

    def test_solution6(self):
        assert solution("021") == "0((2)1)"

    def test_solution7(self):
        assert solution("312") == "(((3))1(2))"

    def test_solution8(self):
        assert solution("4") == "((((4))))"

    def test_solution9(self):
        assert solution("221") == "((22)1)"
