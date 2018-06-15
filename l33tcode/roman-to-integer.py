class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

	prev = ''
        prev_int_value = 0

        result = 0

        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

	for symbol in s:
            current_int_value = roman_to_int_map[symbol]
            result += current_int_value

            if prev and prev_int_value < current_int_value:
                result -= prev_int_value * 2

            prev = symbol
            prev_int_value = roman_to_int_map[prev]

        return result


solution = Solution()

for i in range(100000):
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IX") == 9
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
