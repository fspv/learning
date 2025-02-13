import unittest


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or not s:
            return s

        result = ""

        for row in range(min(num_rows, len(s))):
            shift1 = 2 * (num_rows - (row + 1)) if row != num_rows - 1 else 2 * row
            shift2 = 2 * (num_rows - (row + 1)) if row == 0 else 2 * row
            shift = shift1
            toggle = True
            next_symbol = row
            while next_symbol < len(s):
                result += s[next_symbol]

                if toggle:
                    shift = shift1
                else:
                    shift = shift2

                if not shift:
                    toggle = not toggle
                    continue

                next_symbol += shift
                toggle = not toggle

        return result

    def convertBruteForce(self, s: str, num_rows: int) -> str:
        if not num_rows:
            return ""
        elif num_rows == 1:
            return s

        width = int(len(s) / (2 * num_rows - 2) + 1) * (num_rows - 1)

        matrix: list[list[str]] = [["" for _ in range(width)] for _ in range(num_rows)]

        direction_map = {
            True: (1, 0),
            False: (-1, 1),
        }
        direction = False

        x, y = 0, 0

        for symbol in s:
            matrix[y][x] = symbol

            while True:
                y += direction_map[direction][0]
                x += direction_map[direction][1]

                if not (0 <= y < len(matrix)) or not (0 <= x < len(matrix[0])):
                    y -= direction_map[direction][0]
                    x -= direction_map[direction][1]
                    direction = not direction
                    continue

                break

        result = ""

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column]:
                    result += matrix[row][column]

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.convert("", 0), "")

    def test_empty_one_row(self):
        self.assertEqual(self.sol.convert("", 1), "")

    def test_empty_many_rows(self):
        self.assertEqual(self.sol.convert("", 50), "")

    def test_one(self):
        self.assertEqual(self.sol.convert("A", 0), "")

    def test_one_one_row(self):
        self.assertEqual(self.sol.convert("A", 1), "A")

    def test_one_many_rows(self):
        self.assertEqual(self.sol.convert("A", 50), "A")

    def test_complex1(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_complex2(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_complex3(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 5), "PHASIYIRPLIGAN")

    def test_complex4(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 6), "PRAIIYHNPSGAIL")


if __name__ == "__main__":
    unittest.main()
