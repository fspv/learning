class Solution:
    def letterCombinations(self, digits):
        key_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def guesses(pos):
            if pos == len(digits):
                return [""]

            result = []

            for letter in key_map[digits[pos]]:
                for guess in guesses(pos + 1):
                    result.append(letter + guess)

            return result

        result = guesses(0)

        return result if len(result) > 1 else []


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.letterCombinations("") == []

    def test_custom1(self):
        assert self.sol.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
