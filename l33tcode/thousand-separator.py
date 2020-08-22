class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = []

        numbers = 0

        while n > 0:
            new_number = n % 10
            n //= 10

            if numbers > 0 and numbers % 3 == 0:
                result.append(".")

            result.append(str(new_number))
            numbers += 1

        return "".join(reversed(result)) or "0"
