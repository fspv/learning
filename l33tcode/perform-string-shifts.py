class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_shift = sum((-1) ** d * c for d, c in shift) % len(s)

        return "".join([s[(p + final_shift) % len(s)] for p in range(len(s))])
