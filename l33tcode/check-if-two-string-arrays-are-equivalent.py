from typing import List, Tuple


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        pos1, index1 = 0, 0
        pos2, index2 = 0, 0

        def check_valid_pos(words: List[str], pos: int, index: int) -> bool:
            return pos < len(words) and index < len(words[pos])

        def get_next(words: List[str], pos: int, index: int) -> Tuple[int, int]:
            if check_valid_pos(words, pos, index + 1):
                return pos, index + 1
            else:
                return pos + 1, 0

        while True:
            if word1[pos1][index1] == word2[pos2][index2]:
                pos1, index1 = get_next(word1, pos1, index1)
                pos2, index2 = get_next(word2, pos2, index2)
            else:
                return False

            if not check_valid_pos(word1, pos1, index1) or not check_valid_pos(word2, pos2, index2):
                if not check_valid_pos(word1, pos1, index1) and not check_valid_pos(word2, pos2, index2):
                    break
                else:
                    return False

        return True
