from functools import lru_cache


class Solution:
    def numDecodings(self, encoded: str) -> int:
        MOD = 10 ** 9 + 7

        def get_number_of_options(pos: int, length: int) -> int:
            if length == 1:
                if encoded[pos] == "*":
                    return 9
                elif encoded[pos] == "0":
                    return 0
                else:
                    return 1
            elif length == 2 and pos + length <= len(encoded):
                if encoded[pos:pos + 2] == "**":
                    return 15
                elif encoded[pos] == "*":
                    second_digit = int(encoded[pos + 1])

                    count = 0
                    for first_digit in range(1, 10):
                        if 9 < first_digit * 10 + second_digit < 27:
                            count += 1

                    return count
                elif encoded[pos + 1] == "*":
                    first_digit = int(encoded[pos])

                    count = 0
                    for second_digit in range(1, 10):
                        if 9 < first_digit * 10 + second_digit < 27:
                            count += 1

                    return count
                elif 9 < int(encoded[pos:pos + 2]) < 27:
                    return 1

            return 0

        @lru_cache(None)
        def dp(pos: int) -> int:
            if pos >= len(encoded):
                return 1

            return (
                dp(pos + 1) * get_number_of_options(pos, 1) +
                dp(pos + 2) * get_number_of_options(pos, 2)
            ) % MOD

        def dp_bottom_up() -> int:
            dp_prev, dp_prev_prev = 1, 0

            for pos in reversed(range(len(encoded))):
                dp = (
                    dp_prev * get_number_of_options(pos, 1) +
                    dp_prev_prev * get_number_of_options(pos, 2)
                ) % MOD
                dp_prev, dp_prev_prev = dp, dp_prev

            return dp

        # return dp(0)
        return dp_bottom_up()
