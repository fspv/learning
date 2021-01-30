class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        shift = 1
        target = 2
        result = 0

        for num in range(1, n + 1):
            if target == num:
                shift += 1
                target <<= 1

            result <<= shift
            result |= num

            result %= MOD

        return result
