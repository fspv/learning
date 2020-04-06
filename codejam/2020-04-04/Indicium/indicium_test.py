from indicium import find_possible_sums, find_possible_fill


class TestSolution:
    def test_find_possible_sums1(self):
        assert find_possible_sums(10, 2, 5) == [[2, 2, 2, 2, 2]]

    def test_find_possible_sums2(self):
        for i in range(1):
            assert find_possible_sums(2500, 50, 50) == [[50] * 50]

    def test_find_possible_fill1(self):
        assert find_possible_fill(3, [[2,2,2]]) == [[2,1,3], [3,2,1], [1,3,2]]

    def test_find_possible_fill2(self):
        assert find_possible_fill(50, find_possible_sums(50, 50, 50)) == [[2,1,3], [3,2,1], [1,3,2]]
