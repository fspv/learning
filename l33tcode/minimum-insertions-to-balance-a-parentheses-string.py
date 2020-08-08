from typing import List


class Solution:
    def minInsertions(self, s: str) -> int:
        paren = "("
        back_paren = ")"
        stack: List[str] = []

        transformed = []
        insertions = 0

        pos = 0
        while pos < len(s):
            if s[pos:pos + 2] == "))":
                transformed.append(False)
                pos += 2
            elif s[pos] == "(":
                transformed.append(True)
                pos += 1
            else:
                transformed.append(False)
                pos += 1
                insertions += 1

        stack = []

        for char in transformed:
            if stack and stack[-1] == True:
                if char == False:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return insertions + (len(stack) - sum(stack)) + sum(stack) * 2
