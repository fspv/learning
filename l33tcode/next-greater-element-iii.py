class Solution:
    def nextGreaterElement(self, n: int) -> int:
        array = list(str(n))

        for pos in reversed(range(len(array) - 1)):
            if array[pos] < array[pos + 1]:
                next_pos = pos + 1
                next_greater = next_pos

                while next_pos < len(array) and array[next_pos] > array[pos]:
                    next_greater = next_pos
                    next_pos += 1

                array[pos], array[next_greater] = array[next_greater], array[pos]
                array[pos + 1:] = list(sorted(array[pos + 1:]))
                break

        result = int("".join(array))

        if result == n:
            return -1

        if result & (0xFFFFFFFF >> 1) != result:
            return -1

        return result
