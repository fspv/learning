from typing import List, Tuple


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        taken = [False, False, False, False]

        def get_hour(digits: List[int]) -> Tuple[str, str]:
            for first_pos, first in enumerate(digits):
                for second_pos, second in enumerate(digits):
                    if first_pos == second_pos:
                        continue

                    if (hour := first * 10 + second) < 24:
                        taken[first_pos] = True
                        taken[second_pos] = True
                        minute = get_minute(digits)
                        taken[first_pos] = False
                        taken[second_pos] = False

                        if minute:
                            return str(hour).zfill(2), minute

            return "", ""

        def get_minute(digits: List[int]) -> str:
            for first_pos, first in enumerate(digits):
                for second_pos, second in enumerate(digits):
                    if first_pos == second_pos:
                        continue

                    if taken[first_pos] or taken[second_pos]:
                        continue

                    if (minute := first * 10 + second) < 60:
                        return str(minute).zfill(2)

            return ""

        A.sort(reverse=True)

        hour, minute = get_hour(A)

        if hour and minute:
            return hour + ":" + minute

        return ""
