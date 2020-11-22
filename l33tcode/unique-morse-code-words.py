from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        return len(
            {
                "".join(map(lambda x: alphabet[ord(x) - ord("a")], word))
                for word in words
            }
        )
