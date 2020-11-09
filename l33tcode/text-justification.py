from typing import List


class Text:
    def __init__(self, words: List[str]) -> None:
        self._words = words

    def _get_sum_words_length(self, start: int, end: int) -> int:
        return sum(map(len, self._words[start:end]))

    def _get_fits_width(self, start: int, width: int) -> int:
        pos = start
        total = 0

        while pos < len(self._words) and total + len(self._words[pos]) <= width:
            total += len(self._words[pos]) + 1
            pos += 1

        return pos

    def justify(self, width: int) -> List[str]:
        result: List[str] = []
        start = 0
        while start < len(self._words):
            end = self._get_fits_width(start, width)
            words_length = self._get_sum_words_length(start, end)
            spaces_needed = width - words_length
            sub_result: List[str] = []

            if end == len(self._words):
                sub_result.append(" ".join(self._words[start:end]))
                sub_result.append(" " * (spaces_needed - (end - start - 1)))
            else:
                if end - start > 1:
                    base_spaces = spaces_needed // (end - start - 1)
                    extra_spaces = spaces_needed % (end - start - 1)

                    spaces = " " * base_spaces
                    for pos in range(start, end - 1):
                        sub_result.append(self._words[pos])
                        extra_space = " " if extra_spaces > 0 else ""
                        extra_spaces -= 1
                        sub_result.append(spaces)
                        sub_result.append(extra_space)

                    sub_result.append(self._words[end - 1])
                else:
                    sub_result.append(self._words[end - 1])
                    sub_result.append(" " * spaces_needed)

            result.append("".join(sub_result))

            start = end

        return result


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        text = Text(words)

        return text.justify(maxWidth)
