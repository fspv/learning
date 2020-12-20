from typing import List, Tuple


class Solution:
    def decodeAtIndex(self, string: str, K: int) -> str:
        def gen_array(string: str) -> List[str]:
            def get_word(pos: int) -> Tuple[str, int]:
                start_pos = pos
                while pos < len(string) and not string[pos].isdigit():
                    pos += 1

                return string[start_pos:pos], pos

            pos = 0

            array: List[str] = []

            while pos < len(string):
                if string[pos].isdigit():
                    array.append(string[pos])
                    pos += 1
                else:
                    word, pos = get_word(pos)
                    array.append(word)

            return array

        array = gen_array(string)

        counts = [0]

        for smth in array:
            if smth.isdigit():
                counts.append(counts[-1] * int(smth))
            else:
                counts.append(counts[-1] + len(smth))

            if counts[-1] > K:
                break

        tape_pos = K - 1
        for pos in reversed(range(len(counts))):
            if array[pos - 1].isdigit():
                tape_pos %= counts[pos - 1]
            else:
                if tape_pos >= counts[pos - 1]:
                    return array[pos - 1][tape_pos - counts[pos - 1]]
                else:
                    continue

        # This should not happen
        return ""
