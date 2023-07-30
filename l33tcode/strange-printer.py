from functools import lru_cache
from typing import List, Tuple


class Solution:
    def strangePrinter(self, s: str) -> int:
        array: List[int] = []
        prev = ""

        for char in s:
            if char != prev:
                array.append(ord(char) - ord("a"))

            prev = char

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return 1

            # Print the first character and stop
            result = dp(left + 1, right) + 1

            for mid in range(left + 1, right + 1):
                # Print the first character until `mid` and stop
                if array[left] == array[mid]:
                    result = min(result, dp(left, mid - 1) + dp(mid + 1, right))

            return result

        return dp(0, len(array) - 1)

    def strangePrinterBruteForce(self, s: str) -> int:
        # Easier to work with integers
        array = list(ord(letter) - ord("a") for letter in s)

        offsets = [1] * len(array)

        prev = -1
        for pos in reversed(range(len(array))):
            if prev == array[pos]:
                offsets[pos] = offsets[pos + 1] + 1

            prev = array[pos]

        @lru_cache(None)
        def backtrack(pos: int, print_stack: Tuple[int]) -> int:
            if pos == len(array):
                return 0

            # Regardless if we tried this letter or not try to start anew
            stack = list(print_stack)

            stack.append(array[pos])
            new_print = reuse = backtrack(pos + offsets[pos], tuple(stack)) + 1

            stack = list(print_stack)

            # If in the stack, uwind the stack until this letter
            if array[pos] in stack:
                while stack[-1] != array[pos]:
                    stack.pop()

                reuse = backtrack(pos + offsets[pos], tuple(stack))

            return min(new_print, reuse)

        result = backtrack(0, tuple())
        backtrack.cache_clear()

        return result
