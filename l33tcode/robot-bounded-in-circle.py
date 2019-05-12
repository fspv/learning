class Solution:
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        vec = (0, 1)
        pos = (0, 0)

        for i in instructions:
            if i == "G":
                pos = (pos[0] + vec[0], pos[1] + vec[1])
            elif i == "L":
                vec = - vec[1], vec[0]
            elif i == "R":
                vec = vec[1], - vec[0]

        if vec != (0, 1) or pos == (0, 0):
            return True
        else:
            return False


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.isRobotBounded("GGLLGG") == True

    def test_custom2(self):
        assert self.sol.isRobotBounded("GG") == False

    def test_custom3(self):
        assert self.sol.isRobotBounded("GL") == True

    def test_custom4(self):
        assert self.sol.isRobotBounded("LRRRRLLLRL") == True

    def test_custom4(self):
        assert self.sol.isRobotBounded("RLLGLRRRRGGRRRGLLRRR") == True
