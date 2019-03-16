import unittest


class Solution:
    def getRow(self, rowIndex):
        result = [None] * (rowIndex + 1)
        mem = dict()
        for pos in range(len(result)):
            result[pos] = self.gen_cell(rowIndex, pos, mem)
        return result

    def gen_cell(self, level, pos, mem):
        if pos == 0 or pos == level:
            return 1
        else:
            result = 0
            for prev_level, prev_pos in \
                [(level - 1, pos - 1), (level - 1, pos)]:
                if (prev_level, prev_pos) in mem:
                    result += mem.pop((prev_level, prev_pos))
                else:
                    mem[(prev_level, prev_pos)] = \
                        self.gen_cell(prev_level, prev_pos, mem)
                    result += mem[(prev_level, prev_pos)]
            return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.getRow(0) == [1]

    def test_two(self):
        assert self.sol.getRow(1) == [1, 1]

    def test_three(self):
        assert self.sol.getRow(2) == [1, 2, 1]

    def test_four(self):
        assert self.sol.getRow(3) == [1, 3, 3, 1]

    def test_five(self):
        assert self.sol.getRow(4) == [1, 4, 6, 4, 1]

    def test_six(self):
        assert self.sol.getRow(5) == [1, 5, 10, 10, 5, 1]

    def test_six(self):
        assert self.sol.getRow(33) == [1,33,528,5456,40920,237336,1107568,4272048,13884156,38567100,92561040,193536720,354817320,573166440,818809200,1037158320,1166803110,1166803110,1037158320,818809200,573166440,354817320,193536720,92561040,38567100,13884156,4272048,1107568,237336,40920,5456,528,33,1]


if __name__ == "__main__":
    unittest.main()
