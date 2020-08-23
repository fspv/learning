from collections import Counter


class Solution:
    def _get_hint_cows(self, secret: str, guess: str) -> int:
        same = 0
        for pos in range(len(secret)):
            if secret[pos] == guess[pos]:
                same += 1

        return same

    def _get_hint_bulls(self, secret: str, guess: str) -> int:
        counter_secret = Counter(secret)
        counter_guess = Counter(guess)

        match = 0

        for char, count in counter_secret.items():
            match += min(count, counter_guess[char])

        return match - self._get_hint_cows(secret, guess)

    def getHint(self, secret: str, guess: str) -> str:
        assert len(secret) == len(guess), "Legths of secret and guess should match"

        hint_cows = self._get_hint_cows(secret, guess)
        hint_bulls = self._get_hint_bulls(secret, guess)

        return str(hint_cows) + "A" + str(hint_bulls) + "B"
