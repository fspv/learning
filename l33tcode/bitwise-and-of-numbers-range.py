class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return m >> (m - n).bit_length() << (m - n).bit_length() & n
