def jumpingOnClouds(c):
    level = 0
    stack = [0]

    while stack:
        old_stack = stack
        stack = []

        level += 1

        for pos in old_stack:
            for offset in [1, 2]:
                next_pos = pos + offset
                if next_pos == len(c) - 1:
                    return level
                if next_pos < len(c) - 1 and c[next_pos] == 0:
                    stack.append(next_pos)


class TestJumpingOnClouds:
    def test_custom1(self):
        assert jumpingOnClouds([0,0]) == 1

    def test_custom2(self):
        assert jumpingOnClouds([0, 1, 0, 0, 0, 0]) == 3

    def test_custom3(self):
        assert jumpingOnClouds([0, 0, 0, 0, 1, 0]) == 3

    def test_custom4(self):
        assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) == 4
