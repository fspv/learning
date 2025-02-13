class Number:
    def __init__(self, num: int) -> None:
        self._num = num

        self._roman_numbers = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

    @property
    def roman(self) -> str:
        num = self._num

        result = []
        while num > 0:
            for value, roman_repr in reversed(sorted(self._roman_numbers.items())):
                if num >= value:
                    result.append(roman_repr)
                    num -= value
                    break

        return "".join(result)


class Solution:
    def intToRoman(self, num: int) -> str:
        number = Number(num)

        return number.roman
