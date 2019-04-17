# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n + 1

        while left < right:
            mid = (left + right) // 2

            bad = isBadVersion(mid)

            if bad:
                right = mid
            else:
                left = mid + 1

        if left < n + 1:
            return left

        return -1
