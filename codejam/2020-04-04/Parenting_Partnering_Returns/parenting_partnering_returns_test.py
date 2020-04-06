from parenting_partnering_returns import solution


class TestSolution:
    def test_solution1(self):
        assert solution(iter([(360, 480), (420, 540), (600, 660),])) == [
            True,
            False,
            True,
        ]

    def test_solution2(self):
        assert solution(iter([(0, 1440), (1, 3), (2, 4),])) is None

    def test_solution3(self):
        assert solution(
            iter([(99, 150), (1, 100), (100, 301), (2, 5), (150, 250),])
        ) == [False, True, True, False, False]

    def test_solution4(self):
        assert solution(iter([(0, 720), (720, 1440),])) == [True, True]

    def test_solution5(self):
        assert solution(iter([(0,1), (0,1), (0,1)])) is None

    def test_solution6(self):
        assert solution(iter([(0,1), (0,100), (0,200), (0,400), (0,500)])) is None
