class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x1, x2, y1, y2 = points[0][0], points[1][0], points[0][1], points[1][1]

        a = (y2 - y1)
        b = (y1 * x2 - y2 * x1)

        return points[2][1] * (x2 - x1) != a * points[2][0] + b

class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.isBoomerang([[1,1],[2,3],[3,2]]) == True

    def test_custom2(self):
        assert self.sol.isBoomerang([[1,1],[2,2],[3,3]]) == False

    def test_custom3(self):
        assert self.sol.isBoomerang([[1,2],[2,4],[3,6]]) == False

    def test_custom4(self):
        assert self.sol.isBoomerang([[1,2],[2,4],[3,7]]) == True

    def test_custom4(self):
        assert self.sol.isBoomerang([[0,0],[0,2],[2,1]]) == True
