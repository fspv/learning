from typing import List
from functools import lru_cache


class KPalindrome:
    def __init__(self, input_string: str, k: int) -> None:
        if not self._validate_input(input_string):
            raise ValueError("Input is invalid")

        self._string = input_string
        self._k = k

    def _validate_input(self, input_string: str) -> bool:
        return True

    def _validate_palindrome(self, array: List[str]) -> bool:
        left, right = 0, len(array) - 1

        while left < right:
            if array[left] != array[right]:
                return False
            left += 1
            right -= 1

        return True

    def _backtrack(self, pos: int, skips_left: int) -> bool:
        if pos == len(self._string):
            return self._validate_palindrome(self._stack)

        if skips_left > 0:
            if self._backtrack(pos + 1, skips_left - 1):
                return True

        self._stack.append(self._string[pos])
        self._backtrack(pos + 1, skips_left)
        self._stack.pop()

        return False

    @lru_cache(None)
    def _dp(self, left: int, right: int, skips_left: int) -> bool:
        if left == right:
            return True

        if left + 1 == right and self._string[left] == self._string[right]:
            return True

        result = False

        if self._string[left] == self._string[right]:
            result = result or self._dp(left + 1, right - 1, skips_left)

        if skips_left > 0:
            result = result or self._dp(left + 1, right, skips_left - 1)
            result = result or self._dp(left, right - 1, skips_left - 1)

        return result

    def validate(self) -> bool:
        self._stack: List[str] = []
        # return self._backtrack(0, self._k)
        return self._dp(0, len(self._string) - 1, self._k)


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        palindrome = KPalindrome(s, k)

        return palindrome.validate()
