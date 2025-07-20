class Solution:
    def trap(self, height):
        if not height:
            return 0

        stack = [(height[0], 0)]
        result = 0

        for pos in range(1, len(height)):
            if height[pos] > stack[-1][0]:
                while stack and height[pos] > stack[-1][0]:
                    prev_height, prev_pos = stack.pop()
                    if stack:
                        p_width = pos - stack[-1][1] - 1
                        p_depth = min(height[pos], stack[-1][0]) - prev_height
                        result += p_width * p_depth

            stack.append((height[pos], pos))

        return result

    def trap_dp_long(self, height):
        if not height:
            return 0

        dp = [-1] * max(height)
        result = 0

        for pos in range(len(height)):
            if pos > 0 and height[pos] > height[pos - 1]:
                for h in range(height[pos - 1], height[pos]):
                    if dp[h] != -1:
                        result += pos - dp[h] - 1

            for h in range(height[pos]):
                dp[h] = pos

        return result
    def trap_dp_long(self, height):
        if not height:
            return 0

        dp = [-1] * max(height)
        result = 0

        for pos in range(len(height)):
            if pos > 0 and height[pos] > height[pos - 1]:
                for h in range(height[pos - 1], height[pos]):
                    if dp[h] != -1:
                        result += pos - dp[h] - 1

            for h in range(height[pos]):
                dp[h] = pos

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.trap([]) == 0

    def test_one(self):
        assert self.sol.trap([1]) == 0

    def test_custom1(self):
        assert self.sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

    def test_custom3(self):
        assert self.sol.trap([4,2,0,3,2,5]) == 9

    def test_custom4(self):
        assert self.sol.trap([5,2,1,2,1,5]) == 14
