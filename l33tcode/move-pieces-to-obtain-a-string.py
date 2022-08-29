from typing import Counter


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if Counter(start) != Counter(target):
            return False

        spaces = 0
        start_pos = 0

        start_arr = list(start)
        target_arr = list(target)
        left = "L"

        for _ in range(2):
            for target_pos in range(len(target)):
                if target_arr[target_pos] == "_":
                    continue

                while start_pos < len(start) and start_arr[start_pos] == "_":
                    start_pos += 1
                    spaces += 1

                if (
                    start_pos == len(start_arr)
                    or start_arr[start_pos] != target_arr[target_pos]
                ):
                    return False

                if start_arr[start_pos] == left:
                    if start_pos < target_pos:
                        return False
                    else:
                        if spaces < start_pos - target_pos:
                            return False
                        else:
                            spaces = start_pos - target_pos
                            if start_pos != target_pos:
                                start_arr[target_pos] = target_arr[target_pos]
                                start_arr[start_pos] = "_"
                else:
                    spaces = 0

                start_pos += 1

            start_arr.reverse()
            target_arr.reverse()
            left = "R"
            spaces = 0
            start_pos = 0

        return True
