from typing import Dict


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        def get_positions(keyboard: str) -> Dict[str, int]:
            positions = {}

            for pos, char in enumerate(keyboard):
                positions[char] = pos

            return positions


        moves = 0
        positions = get_positions(keyboard)
        prev_pos = 0

        for char in word:
            cur_pos = positions[char]

            moves += abs(cur_pos - prev_pos)

            prev_pos = cur_pos

        return moves
