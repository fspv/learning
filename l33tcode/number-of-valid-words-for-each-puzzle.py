from typing import Dict, List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # Can use Counter instead, but it is slower

        # Build a number of times bitmap of a word met in a words array
        # Bitmap represents letters exist in the word, it fits integer because
        # alphabet size is 26
        word_map: Dict[int, int] = {}

        for word in words:
            word_hash = 0

            for letter in word:
                word_hash |= 1 << (ord(letter) - ord("a"))

            word_map.setdefault(word_hash, 0)
            word_map[word_hash] += 1

        def dfs(puzzle: str, pos: int, bitmap: int) -> int:
            """
            Try to generate all variations of puzzle bitmap obtained by
            preserving or removing arbitatrary characters
            """
            if pos == len(puzzle):
                return word_map.get(bitmap, 0)

            letter_bitmap = 1 << (ord(puzzle[pos]) - ord("a"))

            count = 0

            # Skip
            if pos != 0:
                # Can't skip the first letter of the puzzle
                count += dfs(puzzle, pos + 1, bitmap)

            # Keep
            count += dfs(puzzle, pos + 1, bitmap | letter_bitmap)

            return count

        count = [0] * len(puzzles)

        for pos, puzzle in enumerate(puzzles):
            # Calculate number of words for each puzzle
            count[pos] = dfs(puzzle, 0, 0)

        return count
