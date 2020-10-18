class Solution:
    def checkValidString(self, s: str) -> bool:
        stars, open_parens, close_parens = 0, 0, 0

        for char in s:
            if char == "(":
                open_parens += 1
            elif char == ")":
                close_parens += 1
            else:
                stars += 1

        return open_parens - stars <= close_parens <= open_parens + stars
