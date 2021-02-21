class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        steps = 0
        while X < Y:
            if Y & 1 == 1:
                Y += 1
            else:
                Y //= 2

            steps += 1

        return steps + (X - Y)
