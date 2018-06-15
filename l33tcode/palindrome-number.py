import sys

class Solution:
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_list = []

        result = x

        while result > 0:
            remains = result % 10
            result //= 10
            x_list.append(remains)

        for pos in range(int(len(x_list) / 2)):
            if x_list[pos] != x_list[len(x_list) - 1 - pos]:
                return False

        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        if x >= 10 and x % 10 == 0:
            return False

	reverted = 0

	while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        return x == reverted or x == reverted // 10

solution = Solution()

assert solution.isPalindrome(10) == False
assert solution.isPalindrome(121) == True
assert solution.isPalindrome(0) == True
assert solution.isPalindrome(-121) == False
assert solution.isPalindrome(123) == False
for i in range(1000000):
    assert solution.isPalindrome(sys.maxint) == False
