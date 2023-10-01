class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)

        def reverse(start: int, stop: int) -> None:
            while start < stop:
                arr[start], arr[stop] = arr[stop], arr[start]
                start += 1
                stop -= 1

        def get_word_length(start: int) -> int:
            stop = start
            while stop < len(arr) and arr[stop] != " ":
                stop += 1

            return stop - start

        start = 0

        while start < len(arr):
            word_length = get_word_length(start)
            reverse(start, start + word_length - 1)
            start += word_length + 1

        return "".join(arr)
