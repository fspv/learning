import string


class String:
    def __init__(self, input_string: str) -> None:
        if set(input_string) - set(string.ascii_lowercase):
            raise ValueError("should be lowercase alphanumeric")
        self._string = input_string

    @property
    def power(self) -> int:
        counter = 1
        prev_char = chr(0)

        max_power = 0

        for char in self._string:
            if char == prev_char:
                counter += 1
            else:
                counter = 1

            max_power = max(max_power, counter)

            prev_char = char

        return max_power


class Solution:
    def maxPower(self, s: str) -> int:
        string_obj = String(s)
        return string_obj.power
