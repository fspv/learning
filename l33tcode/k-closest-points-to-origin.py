import unittest


class Solution:
    def kClosest(self, points, K):
        return sorted(points, key=lambda point: point[0] * point[0] + point[1] * point[1])[:K]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty1(self):
        self.assertListEqual(self.sol.kClosest([], 1), [])

    def test_empty2(self):
        self.assertListEqual(self.sol.kClosest([], 0), [])

    def test_one1(self):
        self.assertListEqual(self.sol.kClosest([[1,1]], 1), [[1,1]])

    def test_one2(self):
        self.assertListEqual(self.sol.kClosest([[1,1]], 2), [[1,1]])

    def test_one3(self):
        self.assertListEqual(self.sol.kClosest([[1,1]], 0), [])

    def test_custom1(self):
        self.assertListEqual(self.sol.kClosest([[1,3],[-2,2]], 1), [[-2,2]])

    def test_custom2(self):
        self.assertListEqual(self.sol.kClosest([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]])


if __name__ == "__main__":
    unittest.main()
