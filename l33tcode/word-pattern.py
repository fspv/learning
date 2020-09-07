from typing import Tuple, Dict


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        def get_letter(pattern: str, pos: int) -> Tuple[str, int]:
            return pattern[pos], pos + 1

        def get_word(string: str, pos: int) -> Tuple[str, int]:
            begin_pos = pos

            while pos < len(string) and string[pos] != " ":
                pos += 1

            return string[begin_pos:pos], pos + 1

        pattern_pos, string_pos = 0, 0

        mapping_fwd: Dict[str, str] = {}
        mapping_back: Dict[str, str] = {}

        while pattern_pos < len(pattern) and string_pos < len(string):
            letter, pattern_pos = get_letter(pattern, pattern_pos)
            word, string_pos = get_word(string, string_pos)

            if letter in mapping_fwd:
                if mapping_fwd[letter] != word:
                    return False
            else:
                mapping_fwd[letter] = word

            if word in mapping_back:
                if mapping_back[word] != letter:
                    return False
            else:
                mapping_back[word] = letter

        if pattern_pos < len(pattern) or string_pos < len(string):
            return False

        return True
