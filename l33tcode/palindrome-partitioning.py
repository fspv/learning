from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start: int, end: int) -> bool:
            end -= 1
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        result: List[List[str]] = []

        def dfs(start: int, path: List[str]) -> None:
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(start, end):
                    path.append(s[start:end])
                    dfs(end, path)
                    path.pop()

        dfs(0, [])

        return result
