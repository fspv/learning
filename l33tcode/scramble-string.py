from typing import List
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        string = list(s1)

        def reverse(left: int, right: int) -> None:
            while left < right - 1:
                string[left], string[right - 1] = string[right - 1], string[left]
                left += 1
                right -= 1

        def swap_subarrays(
            left: int, middle: int, right: int
        ) -> None:
            # reverse all
            reverse(left, right)
            # reverse left
            reverse(left, left + right - middle)
            # reverse right
            reverse(left + right - middle, right)

        def dfs(left: int, right: int) -> bool:
            if right - left == 1:
                return s2[left] == string[left]

            if Counter(string[left:right]) != Counter(s2[left:right]):
                return False

            result = False
            for middle in range(left + 1, right):
                result = result or (
                    dfs(left, middle,) and dfs(middle, right,)
                )

                swap_subarrays(left, middle, right)

                result = result or (
                    dfs(left, left + right - middle,)
                    and dfs(left + right - middle, right,)
                )

                swap_subarrays(left, left + right - middle, right)

            return result

        return dfs(0, len(s1))
