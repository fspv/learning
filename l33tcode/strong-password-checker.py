import string
from typing import List


class StrongPassswordChecker:
    def __init__(self, password: str) -> None:
        self._password = password

    def _has_lowercase(self) -> bool:
        return bool(set(self._password) & set(string.ascii_lowercase))

    def _has_uppercase(self) -> bool:
        return bool(set(self._password) & set(string.ascii_uppercase))

    def _has_digits(self) -> bool:
        return bool(set(self._password) & set(string.digits))

    def _sequences_longer_than_two(self) -> List[int]:
        """
        Return lengths of sequences in the password that have length more than 2
        """
        count = 0
        prev = ""

        sequences = []

        for char in self._password:
            if char == prev:
                count += 1
            else:
                if count > 2:
                    sequences.append(count)
                count = 1

            prev = char

        if count > 2:
            sequences.append(count)

        return sequences

    def to_valid(self) -> int:
        # Amendments we should to to make sure all required types of characters
        # are present in the string
        to_amend = (
            int(not self._has_lowercase())
            + int(not self._has_uppercase())
            + int(not self._has_digits())
        )

        # Replacements we should do in order to break all the sequences having
        # length greater than 2
        longer_than_two = self._sequences_longer_than_two()
        to_replace = sum(map(lambda x: x // 3, longer_than_two))

        modifications = 0

        if len(self._password) <= 20:
            to_add = max(6 - len(self._password), 0)

            modifications = max(to_replace, to_amend, to_add)
        else:
            to_delete = len(self._password) - 20

            # Greedy way to use deletions instead of replacements
            # because there is a chance we can save some replacements
            # this way and hence get less modificaions
            while to_delete > 0 and longer_than_two:
                last = longer_than_two.pop()
                while last > 2:
                    can_delete = last % 3 + 1
                    if can_delete <= to_delete:
                        to_delete -= can_delete
                        last -= can_delete
                        to_replace -= 1
                    else:
                        break

            # Restore to_delete, since we're making deletions no matter what.
            # But we probably reduced the number of replacements on the previous
            # step
            to_delete = len(self._password) - 20

            modifications = max(to_replace, to_amend) + to_delete

        return modifications


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        checker = StrongPassswordChecker(s)

        return checker.to_valid()
