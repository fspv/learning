from functools import lru_cache


class Solution:
    def removePalindromeSub(self, string: str) -> int:
        def is_palindrome(left: int, right: int) -> bool:
            right -= 1

            while left < right:
                if string[left] != string[right]:
                    return False

                left += 1
                right -= 1

            return True

        @lru_cache(None)
        def dp(pos: int) -> int:
            if pos == len(string):
                return 0

            min_steps = len(string)
            for next_pos in range(pos + 1, len(string) + 1):
                if is_palindrome(pos, next_pos):
                    min_steps = min(min_steps, dp(next_pos) + 1)

            return min_steps

        return dp(0)
