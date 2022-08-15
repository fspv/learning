from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result: List[int] = []

        num1, num2 = num, list(map(int, str(k)))

        if len(num2) > len(num1):
            num1, num2 = num2, num1

        carry = 0

        for pos in range(len(num1)):
            digit1, digit2 = num1[-pos - 1], num2[-pos - 1] if pos < len(num2) else 0

            digit = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10

            result.append(digit)

        if carry > 0:
            result.append(carry)

        return list(reversed(result))
