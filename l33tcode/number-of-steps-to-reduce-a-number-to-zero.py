class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num > 1:
            steps += (num & 1) + 1
            num >>= 1

        return steps + num
