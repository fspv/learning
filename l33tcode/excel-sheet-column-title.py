from typing import List


class Solution:
    def convertToTitle(self, num: int) -> str:
        column: List[int] = []

        while num:
            column.append((num - 1) % 26)
            num = (num - 1) // 26

        return "".join(reversed(list(map(lambda c: chr(ord("A") + c), column))))
