class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        result = 1

        # C = N! / (K! * (N - K)!)
        # N = n + k - 1
        # K = 2 * k
        # C = (n + k - 1)! / ((2 * k)! * (n + k - 1 - 2 * k)!)
        # C = ((n - k) * ... * (n + k - 1)) / (1 * ... * (2 * k))

        numerator = 1
        for num in range(n - k, n + k):
            numerator *= num

        denominator = 1

        for num in range(1, 2 * k + 1):
            denominator *= num

        return (numerator // denominator) % (10 ** 9 + 7)
