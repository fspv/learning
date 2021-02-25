from typing import List


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack: List[int] = [0]

        for char in S:
            if char == "(":
                stack.append(0)
            else:
                top = stack.pop()

                stack[-1] += max(top * 2, 1)

        return stack[-1]
