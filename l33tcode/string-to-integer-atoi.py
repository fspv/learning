class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        pos = 0
        total = 0
        sign = 1
        limit = ~(-1 << 31)

        while pos < len(s) and s[pos] == " ":
            pos += 1

        if pos < len(s) and s[pos] == "-":
            limit = ~limit
            sign = -1
            pos += 1
        elif pos < len(s) and s[pos] == "+":
            pos += 1

        while pos < len(s) and s[pos].isdigit():
            if total > sign * (limit - sign * int(s[pos])) // 10:
                total = limit * sign
                break

            total *= 10
            total += int(s[pos])
            pos += 1

        return total * sign
