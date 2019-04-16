class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        overflow = 1

        for pos in reversed(range(len(digits))):
            digits[pos] += overflow
            overflow = 0
            if digits[pos] > 9:
                digits[pos] = 0
                overflow = 1

        if overflow == 1:
            digits.insert(0, 1)

        return digits
