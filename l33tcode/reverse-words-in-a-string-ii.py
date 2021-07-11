from typing import Iterator, List, Tuple


class Solution:
    def reverseWords(self, string: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(left: int, right: int) -> None:
            while left < right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1

        def words() -> Iterator[Tuple[int, int]]:
            left, right = 0, 0

            while left < len(string):
                while right < len(string) and string[right] != " ":
                    right += 1

                yield left, right - 1

                left, right = right + 1, right + 1

        reverse(0, len(string) - 1)

        for left, right in words():
            reverse(left, right)
