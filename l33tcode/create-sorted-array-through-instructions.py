from typing import List, Dict


class FenwickTree:
    def __init__(self, size: int) -> None:
        self._container = [0] * (size + 1)

    @staticmethod
    def _least_significant_bit(num: int) -> int:
        return num & (-num)

    def sum(self, pos: int) -> int:
        pos += 1
        result = 0

        while pos > 0:
            result += self._container[pos]
            pos -= self._least_significant_bit(pos)

        return result

    def add(self, pos: int, value: int) -> None:
        pos += 1
        while pos < len(self._container):
            self._container[pos] += value
            pos += self._least_significant_bit(pos)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        instructions_set = set(instructions)

        def create_pos_map() -> Dict[int, int]:
            return {
                instruction: pos
                for pos, instruction in enumerate(sorted(instructions_set))
            }

        pos_map = create_pos_map()
        fenwick_tree = FenwickTree(len(instructions_set))
        added = 0
        score = 0

        for instruction in instructions:
            pos = pos_map[instruction]

            left, this = fenwick_tree.sum(pos - 1), fenwick_tree.sum(pos)
            right = added - this

            score = (score + min(left, right)) % MOD

            fenwick_tree.add(pos, 1)
            added += 1

        return score
