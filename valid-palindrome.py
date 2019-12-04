import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        allowed = set(string.ascii_letters + string.digits)

        while left < right:
            while s[left] not in allowed and left < right:
                left += 1

            while s[right] not in allowed and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.isPalindrome("")

    def test_one(self):
        assert self.sol.isPalindrome("a")

    def test_case1(self):
        assert self.sol.isPalindrome("A man, a plan, a canal: Panama")

    def test_case2(self):
        assert not self.sol.isPalindrome("race a car")

    def test_case3(self):
        assert self.sol.isPalindrome("...................aaa...")

    def test_case4(self):
        assert self.sol.isPalindrome("......................")
