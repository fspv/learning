class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y

        distance = 0

        while num:
            distance += 1
            num &= num - 1

        return distance
