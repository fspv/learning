from typing import List


class Solution:
    def solve(self, s: str) -> str:
        def find_min(string: List[str], pos: int) -> int:
            left = int(string[pos - 1]) if pos > 0 else -1
            right = (
                int(string[pos + 1])
                if pos < len(string) - 1 and string[pos + 1] != "?"
                else -1
            )

            for digit in range(1, 4):
                if digit != left and digit != right:
                    return digit

            return -1

        result: List[str] = list(s)

        for pos in range(len(s)):
            if s[pos] == "?":
                result[pos] = str(find_min(result, pos))

        return "".join(result)
