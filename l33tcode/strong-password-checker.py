from typing import List
import string


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
        to_fix = 0
        to_fix += int(not self._has_lowercase())
        to_fix += int(not self._has_uppercase())
        to_fix += int(not self._has_digits())

        longer_than_two = sum(
            map(lambda x: x // 3, self._sequences_longer_than_two())
        )
        to_modify = longer_than_two

        if 6 <= len(self._password) < 20:
            return max(to_modify, to_fix)
        elif len(self._password) > 20:
            to_delete = len(self._password) - 20

            longer_than_two_arr = self._sequences_longer_than_two()

            while to_delete > 0 and longer_than_two_arr:
                last = longer_than_two_arr.pop()
                while last > 2:
                    can_delete = last % 3 + 1
                    if can_delete <= to_delete:
                        to_delete -= can_delete
                        last -= can_delete
                        to_modify -= 1
                    else:
                        break

            return max(to_fix, to_modify) + len(self._password) - 20
        else:
            to_add = 6 - len(self._password)

            return max(to_add, to_modify, to_fix)


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        checker = StrongPassswordChecker(s)

        return checker.to_valid()
