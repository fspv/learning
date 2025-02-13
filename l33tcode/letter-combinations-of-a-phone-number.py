class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        key_map: dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        stack: list[str] = []
        result: list[str] = []

        def combinations(pos: int) -> None:
            if pos == len(digits):
                if stack:
                    result.append("".join(stack))
                return

            for letter in key_map[digits[pos]]:
                stack.append(letter)
                combinations(pos + 1)
                stack.pop()

        combinations(0)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.letterCombinations("") == []

    def test_custom1(self):
        assert self.sol.letterCombinations("23") == [
            "ad",
            "ae",
            "af",
            "bd",
            "be",
            "bf",
            "cd",
            "ce",
            "cf",
        ]
