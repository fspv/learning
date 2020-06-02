class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = []
        vowels = set("aeiou")

        for pos, word in enumerate(S.split(" ")):
            if word[0].lower() not in vowels:
                word = word[1:] + word[0]

            word = word + "ma" + "a" * (pos + 1)
            words.append(word)

        return " ".join(words)
