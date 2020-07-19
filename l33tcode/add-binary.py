class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        num_a, num_b = int(a, 2), int(b, 2)

        while num_b:
            add = num_a ^ num_b
            carry = (num_a & num_b) << 1
            num_a, num_b = add, carry

        return bin(num_a)[2:]
