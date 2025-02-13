class Solution:
    def reverse(self, x: int) -> int:
        if x == abs(x):
            sign = 1
        else:
            sign = -1

        integer_part = abs(x)

        result = 0

        while integer_part != 0:
            tmp_var = integer_part
            integer_part = tmp_var // 10
            remains = tmp_var % 10
            result = result * 10 + remains

        if abs(result) > 0x7FFFFFFF:
            return 0
        else:
            return result * sign
