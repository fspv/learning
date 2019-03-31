import unittest
from collections import deque

class Solution:
    def numEnclaves(self, A):
        visited = set()
        enclaves_count = 0

        for y in range(len(A)):
            for x in range(len(A[0])):
                if (x, y) not in visited and int(A[y][x]):

                    stack = [(x, y)]
                    visited.add((x, y))
                    out_of_bounds = False
                    count_of_points = 1

                    while len(stack):
                        point = stack.pop()

                        neighbours = [
                            (point[0] - 1, point[1]),
                            (point[0] + 1, point[1]),
                            (point[0], point[1] + 1),
                            (point[0], point[1] - 1),
                        ]

                        for neigh in neighbours:
                            if neigh[0] >= len(A[0]) or neigh[0] < 0 or \
                               neigh[1] >= len(A) or neigh[1] < 0:
                                out_of_bounds = True
                                continue

                            if not int(A[neigh[1]][neigh[0]]):
                                continue

                            if neigh not in visited:
                                count_of_points += 1
                                stack.append(neigh)
                                visited.add(neigh)

                    if not out_of_bounds:
                        enclaves_count += count_of_points

        return enclaves_count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.numEnclaves([]), 0)

    def test_just_zero(self):
        self.assertEqual(self.sol.numEnclaves([[0]]), 0)

    def test_just_one(self):
        self.assertEqual(self.sol.numEnclaves([[1]]), 0)

    def test_1(self):
        A = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 0)

    def test_2(self):
        A = [
            [1, 1, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 0)

    def test_3(self):
        A = [
            [0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 1],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 0)

    def test_4(self):
        A = [
            [0,0,0,0],
            [1,0,1,0],
            [0,1,1,0],
            [0,0,0,0],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 3)

    def test_5(self):
        A = [
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,0,0],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 0)

    def test_6(self):
        A = [
            [0,0,0,0],
            [0,0,1,0],
            [0,1,0,0],
            [0,0,0,0],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 2)

    def test_6(self):
        A = [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 4)

    def test_7(self):
        A = [
            [0,0,0,1,1,1,0,1,0,0],
            [1,1,0,0,0,1,0,1,1,1],
            [0,0,0,1,1,1,0,1,0,0],
            [0,1,1,0,0,0,1,0,1,0],
            [0,1,1,1,1,1,0,0,1,0],
            [0,0,1,0,1,1,1,1,0,1],
            [0,1,1,0,0,0,1,1,1,1],
            [0,0,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,0,0,0,0],
            [0,0,0,0,1,1,0,0,0,1],
        ]
        self.assertEqual(self.sol.numEnclaves(A), 3)


unittest.main()
