import unittest


class Solution:
    def updateMatrix(self, matrix):
        output = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    continue

                stack = [(y, x)]
                visited = set()
                level = 1

                while stack:
                    stack_old = stack
                    stack = []
                    for new_y, new_x in stack_old:
                        visited.add((new_y, new_x))

                        for tmp_y, tmp_x in [
                            (new_y, new_x + 1),
                            (new_y, new_x - 1),
                            (new_y + 1, new_x),
                            (new_y - 1, new_x),
                        ]:
                            if 0 <= tmp_y < len(matrix) and \
                               0 <= tmp_x < len(matrix[0]) and \
                               not (tmp_y, tmp_x) in visited:
                                if matrix[tmp_y][tmp_x] == 0:
                                    output[y][x] = level
                                    break
                                else:
                                    stack.append((tmp_y, tmp_x))
                        else:
                            continue
                        break
                    else:
                        level += 1
                        continue

                    break

        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_element(self):
        self.assertListEqual(self.sol.updateMatrix([[0]]), [[0]])

    def test_two_element(self):
        self.assertListEqual(self.sol.updateMatrix([[0], [0]]), [[0], [0]])

    def test_two_element_2(self):
        self.assertListEqual(self.sol.updateMatrix([[0, 0]]), [[0, 0]])

    def test_two_element_3(self):
        self.assertListEqual(self.sol.updateMatrix([[0, 1]]), [[0, 1]])

    def test_case1(self):
        self.assertListEqual(self.sol.updateMatrix([[0,1,1],[1,1,1],[1,1,1]]), [[0,1,2],[1,2,3],[2,3,4]])

    def test_case2(self):
        self.assertListEqual(self.sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]), [[0,0,0],[0,1,0],[1,2,1]])

    def test_case3(self):
        self.assertListEqual(self.sol.updateMatrix([[0,0,0],[0,0,0],[0,0,0]]), [[0,0,0],[0,0,0],[0,0,0]])

    def test_case4(self):
        self.assertListEqual(self.sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]), [[0,0,0],[0,1,0],[0,0,0]])


if __name__ == "__main__":
    unittest.main()
