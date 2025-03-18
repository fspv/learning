from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def sum_next_k(pos: int) -> int:
            total = 0
            for next_pos in range(pos + 1, pos + abs(k) + 1):
                real_pos = next_pos % len(code)
                total += code[real_pos]

            return total

        decrypted = [0] * len(code)

        for pos in range(len(code)):
            if k > 0:
                decrypted[pos] = sum_next_k(pos)
            elif k < 0:
                decrypted[pos] = sum_next_k(pos + k - 1)

        return decrypted
