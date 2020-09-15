from typing import Tuple


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        def get_word(pos: int) -> Tuple[int, int]:
            word_length = 0
            while pos < len(s) and s[pos] != " ":
                pos += 1
                word_length += 1

            return word_length, pos

        pos = 0
        last_word_length = 0

        while pos < len(s):
            if s[pos] == " ":
                pos += 1
            else:
                last_word_length, pos = get_word(pos)

        return last_word_length
