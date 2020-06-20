from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        power_to_word = {
            3: "Thousand",
            6: "Million",
            9: "Billion",
        }

        digit_to_word = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }

        teen_to_word = {
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        dozen_to_word = {
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        def decimal(result: List[str], num: int):
            if num == 0:
                pass
            elif num % 10 == 0:
                result.append(dozen_to_word[num // 10])
            elif num < 10:
                result.append(digit_to_word[num])
            elif num < 20:
                result.append(teen_to_word[num])
            else:
                result.append(dozen_to_word[num // 10])
                result.append(digit_to_word[num % 10])

        def hundred(result: List[str], num: int):
            if num >= 100:
                result.append(digit_to_word[num // 100])
                result.append("Hundred")

            decimal(result, num % 100)

        def process(num: int) -> str:
            result = []

            for power in [9, 6, 3, 0]:
                if num // (10 ** power) > 0:
                    hundred(result, num // (10 ** power))
                    if power > 0:
                        result.append(power_to_word[power])
                num %= 10 ** power

            return " ".join(result) if result else "Zero"

        return process(num)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.numberToWords(123) == "One Hundred Twenty Three"

    def test_case2(self):
        assert (
            self.sol.numberToWords(123123)
            == "One Hundred Twenty Three Thousand One Hundred Twenty Three"
        )

    def test_case3(self):
        assert (
            self.sol.numberToWords(123123123)
            == "One Hundred Twenty Three Million One Hundred Twenty Three Thousand One Hundred Twenty Three"
        )

    def test_case4(self):
        assert (
            self.sol.numberToWords(123123123123)
            == "One Hundred Twenty Three Billion One Hundred Twenty Three Million One Hundred Twenty Three Thousand One Hundred Twenty Three"
        )

    def test_case5(self):
        assert self.sol.numberToWords(0) == "Zero"

    def test_case6(self):
        assert self.sol.numberToWords(110) == "One Hundred Ten"

    def test_case7(self):
        assert self.sol.numberToWords(150) == "One Hundred Fifty"

    def test_case8(self):
        assert self.sol.numberToWords(50) == "Fifty"

    def test_case9(self):
        assert self.sol.numberToWords(100) == "One Hundred"
