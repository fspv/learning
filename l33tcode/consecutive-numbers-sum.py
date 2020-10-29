class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        arithmetic_progression_sum = 0
        result = 0

        for count in range(1, N + 1):
            arithmetic_progression_sum += count

            if (N - arithmetic_progression_sum) / count + 1 < 1:
                break

            if (N - arithmetic_progression_sum) % count == 0:
                result += 1

        return result
