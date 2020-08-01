import string
from enum import Enum


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        class Constraint(Enum):
            UPPERCASE = 0
            LOWERCASE = 1
            BOTH = 2

        constraint = Constraint.BOTH

        for pos, letter in enumerate(word):
            if letter in string.ascii_lowercase:
                if constraint == Constraint.UPPERCASE:
                    return False
                constraint = Constraint.LOWERCASE
            else:
                if constraint == Constraint.LOWERCASE:
                    return False

                if pos != 0:
                    constraint = Constraint.UPPERCASE

        return True
