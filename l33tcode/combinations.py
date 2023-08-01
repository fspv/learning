from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        stack: List[int] = []

        def combinations(num: int, left: int) -> None:
            if left == 0:
                if num == 0:
                    result.append(stack.copy())
                return

            if num == 0:
                return

            stack.append(num)

            for next_num in reversed(range(num)):
                combinations(next_num, left - 1)

            stack.pop()

        for num in range(n):
            combinations(num + 1, k)

        return result

    def combine1(self, n: int, k: int) -> List[List[int]]:
        def combinations(pos, kk):
            if pos + kk > n + 1:
                return []

            if kk == 0:
                return [[]]

            result = []
            for r_pos in range(pos, n + 1):
                for comb in combinations(r_pos + 1, kk - 1):
                    result.append([r_pos] + comb)

            return result

        return combinations(1, k)
