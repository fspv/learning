import unittest
from collections import deque


class Solution:
    def next_codes(self, code):
        result = []

        for pos in range(len(code)):
            new_char = str((int(code[pos]) + 1) % 10)
            result.append(code[:pos] + new_char + code[(pos + 1):])

            new_char = str((int(code[pos]) - 1) % 10)
            result.append(code[:pos] + new_char + code[(pos + 1):])

        return result


    def openLock(self, deadends, target):
        queue = deque()
        visited = {}
        moves = -1
        level_width = 0

        queue.append("0000")

        while len(queue):
            if level_width == 0:
                level_width = len(queue)
                moves += 1

            code = queue.popleft()
            level_width -= 1

            if code in visited:
                continue

            visited[code] = True

            if code in deadends:
                continue

            if code == target:
                return moves

            for next_code in self.next_codes(code):
                queue.append(next_code)

        return -1



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_already_there(self):
        self.assertEqual(self.sol.openLock(deadends=[], target="0000"), 0)

    def test_simple_1(self):
        self.assertEqual(self.sol.openLock(deadends=[], target="0001"), 1)

    def test_simple_2(self):
        self.assertEqual(self.sol.openLock(deadends=[], target="0101"), 2)

    def test_simple_3(self):
        self.assertEqual(self.sol.openLock(deadends=["0001"], target="0001"), -1)

    def test_simple_4(self):
        self.assertEqual(self.sol.openLock(deadends=["0001"], target="0101"), 2)

    def test_simple_5(self):
        self.assertEqual(self.sol.openLock(deadends=["8888"], target="0009"), 1)

    def test_already_there_and_deadend(self):
        self.assertEqual(self.sol.openLock(deadends=["0000"], target="0000"), -1)

    def test_not_there_and_deadend(self):
        self.assertEqual(self.sol.openLock(deadends=["0000"], target="8888"), -1)

    def test_complex_1(self):
        self.assertEqual(self.sol.openLock(deadends=["0201","0101","0102","1212","2002"], target="0202"), 6)

    def test_complex_2(self):
        self.assertEqual(self.sol.openLock(deadends=["8887","8889","8878","8898","8788","8988","7888","9888"], target="8888"), -1)


unittest.main()
