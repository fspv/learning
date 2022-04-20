import math


class Solution:
    def numWays(self, string: str) -> int:
        ones_total = string.count("1")

        if ones_total == 0:
            return (
                math.factorial(len(string) - 1)
                // 2
                // (math.factorial(len(string) - 3))
            ) % (10 ** 9 + 7)

        if ones_total % 3 != 0:
            return 0

        sep_left_start, sep_left_end = len(string), len(string)
        sep_right_start, sep_right_end = len(string), len(string)

        ones = 0

        for pos in range(len(string)):
            ones += string[pos] == "1"

            if ones == ones_total // 3:
                sep_left_start = min(sep_left_start, pos)

            if ones == ones_total // 3 + 1:
                sep_left_end = min(sep_left_end, pos)

            if ones == (ones_total // 3) * 2:
                sep_right_start = min(sep_right_start, pos)

            if ones == (ones_total // 3) * 2 + 1:
                sep_right_end = min(sep_right_end, pos)

        return ((sep_left_end - sep_left_start) * (sep_right_end - sep_right_start)) % (
            10 ** 9 + 7
        )
