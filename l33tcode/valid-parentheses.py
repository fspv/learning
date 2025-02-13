class Solution:
    def isValid(self, s: str) -> bool:
        valid_open_brackets = {"(", "{", "["}
        valid_close_brackets = {")", "}", "]"}
        close_open_brackets_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        brackets_stack = []

        result = True

        for symbol in s:
            if symbol in valid_open_brackets:
                brackets_stack.append(symbol)
            elif symbol in valid_close_brackets:
                if (
                    len(brackets_stack) == 0
                    or close_open_brackets_map[symbol] != brackets_stack.pop()
                ):
                    result = False
                    break

        if len(brackets_stack) > 0:
            result = False

        return result


solution = Solution()

for i in range(1000000):
    assert solution.isValid("") == True
    assert solution.isValid("[") == False
    assert solution.isValid(")") == False
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("{[]}") == True
