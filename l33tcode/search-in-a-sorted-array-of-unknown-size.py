# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 10001

        while left < right:
            middle = left + (right - left) // 2

            if reader.get(middle) > target:
                right = middle
            elif reader.get(middle) < target:
                left = left + 1
            else:
                return middle

        return -1
