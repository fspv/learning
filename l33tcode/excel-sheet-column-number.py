class Solution:
    def titleToNumber(self, s: str) -> int:
        def char_to_int(s: str) -> int:
            return ord(s) - ord("A") + 1

        def number_of_letters() -> int:
            return char_to_int("Z")

        result = 0

        for char in s:
            result *= number_of_letters()
            result += char_to_int(char)

        return result
