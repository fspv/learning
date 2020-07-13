import string
from enum import Enum


class Solution:
    def calculate(self, s: str) -> int:
        result = 0

        class Operation(Enum):
            ADD = 1
            SUBSTRACT = 2
            MULTIPLY = 3
            DIVIDE = 4

        def get_operation(pos, s):
            if s[pos] == "+":
                return pos + 1, Operation.ADD
            elif s[pos] == "-":
                return pos + 1, Operation.SUBSTRACT
            elif s[pos] == "*":
                return pos + 1, Operation.MULTIPLY
            elif s[pos] == "/":
                return pos + 1, Operation.DIVIDE
            elif s[pos] in string.digits:
                return pos, Operation.ADD
            else:
                raise NotImplementedError(f"Operation {s[pos]} is not implemented")

        def get_number(pos, s):
            number = 0

            while pos < len(s) and s[pos] in string.digits:
                number = number * 10 + int(s[pos])
                pos += 1

            return pos, number

        s = s.replace(" ", "")
        pos = 0
        prev = 0
        while pos < len(s):
            pos, operation = get_operation(pos, s)  # true + , false -
            pos, number = get_number(pos, s)
            if operation == Operation.ADD:
                result += number
                prev = number
            elif operation == Operation.SUBSTRACT:
                result -= number
                prev = -number
            elif operation == Operation.MULTIPLY:
                result -= prev
                result += prev * number
                prev = prev * number
            elif operation == Operation.DIVIDE:
                if number == 0:
                    raise ZeroDivisionError("Cannot divide by zero")

                result -= prev
                result += int(prev / number)
                prev = int(prev / number)

        return result
