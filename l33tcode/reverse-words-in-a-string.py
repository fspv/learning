class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_range(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        def get_words_pos(arr):
            pos = 0
            while pos < len(arr):
                while pos < len(arr) and arr[pos] == " ":
                    pos += 1

                pos_begin = pos

                while pos < len(arr) and arr[pos] != " ":
                    pos += 1

                if pos_begin < pos:
                    yield pos_begin, pos - 1

        arr = list(s)
        reverse_range(arr, 0, len(arr) - 1)

        for start, end in get_words_pos(arr):
            reverse_range(arr, start, end)

        return " ".join(["".join(arr[s:e + 1]) for s, e in get_words_pos(arr)])

    def reverseWords1(self, s: str) -> str:
        def get_prev_word(pos, s):
            while pos >= 0:
                while pos >= 0 and s[pos] == " ":
                    pos -= 1

                pos_end = pos

                while pos >= 0 and s[pos] != " ":
                    pos -= 1

                if pos != pos_end:
                    yield s[pos + 1:pos_end + 1]

        return " ".join(list(get_prev_word(len(s) - 1, s)))
