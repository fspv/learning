from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length
        range_cache = [0] * length

        for begin, end, value in updates:
            range_cache[0 if begin < 0 else begin] += value
            if end + 1 < length:
                range_cache[end + 1] -= value

        value = 0
        for pos in range(length):
            value += range_cache[pos]
            result[pos] = value

        return result

    def getModifiedArray1(self, length: int, updates: List[List[int]]) -> List[int]:
        stack_begin = list(sorted(updates, key=lambda x: -x[0]))
        stack_end = list(sorted(updates, key=lambda x: -x[1]))

        value = 0
        result = [0] * length

        for pos in range(length):
            while stack_begin and stack_begin[-1][0] <= pos:
                value += stack_begin[-1][2]
                stack_begin.pop()

            while stack_end and stack_end[-1][1] < pos:
                value -= stack_end[-1][2]
                stack_end.pop()

            result[pos] = value

        return result
