class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def match(pos: int) -> bool:
            return sequence[pos : (pos + len(word))] == word

        max_repeats = 0
        for pos in range(len(sequence)):
            repeats = 0

            start = pos
            while match(start):
                start += len(word)
                repeats += 1

            max_repeats = max(repeats, max_repeats)

        return max_repeats
