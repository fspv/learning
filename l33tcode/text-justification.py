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

    def fullJustify2(self, words: List[str], max_width: int) -> List[str]:
        word = 0

        def fits_line(word: int, max_width: int) -> int:
            total_len = 0
            count = 0

            while (
                word < len(words)
                and total_len + (len(words[word]) + 1) <= max_width + 1
            ):
                total_len += len(words[word]) + 1
                word += 1
                count += 1

            return count

        def justify_left(start, count, max_width) -> str:
            words_len = sum([len(w) for w in words[start : start + count]])

            return " ".join(words[start : start + count]) + " " * (
                max_width - (count - 1) - words_len
            )

        def justify(start, count, max_width) -> str:
            if count == 1:
                return words[start] + " " * (max_width - len(words[start]))

            words_len = sum([len(w) for w in words[start : start + count]])
            spaces = (max_width - words_len) // (count - 1)
            extra = (max_width - words_len) % (count - 1)

            tmp: List[str] = []

            for word in words[start : start + count - 1]:
                tmp.append(word)
                tmp.append(" " * spaces)
                if extra > 0:
                    tmp.append(" ")
                    extra -= 1

            tmp.append(words[start + count - 1])

            return "".join(tmp)

        result: List[str] = []

        while word < len(words):
            count = fits_line(word, max_width)
            if word + count == len(words):
                line = justify_left(word, count, max_width)
            else:
                line = justify(word, count, max_width)
            result.append(line)
            word += count

        return result
