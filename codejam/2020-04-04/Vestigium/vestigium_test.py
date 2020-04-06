from vestigium import read_matrix, parse_input, solution


class TestSolution:
    def test_read_matrix1(self):
        lines = (
            l for l in ["1 2 3", "1 2 3", "1 2 3",]
        )

        assert list(read_matrix(lines, 3)) == [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
        ]

    def test_read_matrix2(self):
        lines = (
            l for l in ["1",]
        )

        assert list(read_matrix(lines, 1)) == [
            [1],
        ]

    def test_read_matrix3(self):
        lines = (l for l in [])

        assert list(read_matrix(lines, 0)) == []

    def test_parse_input0(self):
        lines = (
            l for l in ["0",]
        )

        sizes = (s for s in [])

        result = (r for r in [])
        for size, matrix in parse_input(lines):
            assert size == next(sizes)
            assert list(matrix) == next(result)

    def test_parse_input1(self):
        lines = (
            l for l in ["1", "1", "1",]
        )

        sizes = (s for s in [1])

        result = (
            r for r in [[[1]],]
        )
        for size, matrix in parse_input(lines):
            assert size == next(sizes)
            assert list(matrix) == next(result)

    def test_parse_input2(self):
        lines = (
            l for l in ["2", "1", "1", "2", "1 1", "1 1",]
        )

        sizes = (s for s in [1, 2])

        result = (r for r in [[[1]], [[1, 1], [1, 1],]])
        for size, matrix in parse_input(lines):
            assert size == next(sizes)
            assert list(matrix) == next(result)

    def test_parse_input3(self):
        lines = (
            l for l in ["2", "1", "1", "2", "1 1", "1 1", "4 3", "12 8",]
        )

        sizes = (s for s in [1, 2])

        result = (r for r in [[[1]], [[1, 1], [1, 1],]])
        for size, matrix in parse_input(lines):
            assert size == next(sizes)
            assert list(matrix) == next(result)

    def test_solution1(self):
        assert solution(1, iter([[1]])) == (1, 0, 0)

    def test_solution2(self):
        assert solution(2, iter([[1, 1], [1, 1]])) == (2, 2, 2)

    def test_solution3(self):
        matrix = [
            [1, 2, 3, 4],
            [2, 1, 4, 3],
            [3, 4, 1, 2],
            [4, 3, 2, 1],
        ]
        assert solution(4, iter(matrix)) == (4, 0, 0)

    def test_solution4(self):
        matrix = [
            [2, 2, 2, 2],
            [2, 3, 2, 3],
            [2, 2, 2, 3],
            [2, 2, 2, 2],
        ]
        assert solution(4, iter(matrix)) == (9, 4, 4)

    def test_solution5(self):
        matrix = [
            [2, 1, 3],
            [1, 3, 2],
            [1, 2, 3],
        ]
        assert solution(3, iter(matrix)) == (8, 0, 2)
