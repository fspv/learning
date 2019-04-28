class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence_str = " ".join(sentence) + " "
        sentence_str_len = len(sentence_str)
        ptr = 0

        for row in range(rows):
            ptr += cols - 1
            if sentence_str[ptr % sentence_str_len] == " ":
                ptr += 1
            elif sentence_str[(ptr + 1) % sentence_str_len] == " ":
                ptr += 2
            else:
                while ptr > 0 and sentence_str[(ptr - 1) % sentence_str_len] != " ":
                    ptr -= 1

        return ptr // sentence_str_len
