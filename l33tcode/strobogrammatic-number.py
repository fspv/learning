class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rot_map = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }

        left, right = 0, len(num) - 1

        while left <= right:
            if rot_map.get(num[left], "a") != num[right]:
                return False
            left, right = left + 1, right - 1

        return True

class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.isStrobogrammatic("") == True

    def test_one2(self):
        assert self.sol.isStrobogrammatic("8") == True

    def test_one3(self):
        assert self.sol.isStrobogrammatic("5") == False

    def test_custom1(self):
        assert self.sol.isStrobogrammatic("69") == True

    def test_custom2(self):
        assert self.sol.isStrobogrammatic("82") == False

    def test_custom3(self):
        assert self.sol.isStrobogrammatic("962") == False

