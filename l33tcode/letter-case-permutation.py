from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result: List[str] = []

        def backtrack(pos: int, path: List[str]) -> None:
            if pos == len(S):
                result.append("".join(path))
                return

            for char in {S[pos].lower(), S[pos].upper()}:
                path.append(char)
                backtrack(pos + 1, path)
                path.pop()

        backtrack(0, [])

        return result
