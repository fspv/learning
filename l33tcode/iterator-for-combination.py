from typing import Tuple


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._stack = list(range(combinationLength))
        self._length = combinationLength
        self._chars = characters

    def _next_char(self, pos) -> Tuple[bool, str]:
        # return exists, next_char
        if pos < len(self._chars) - 1:
            return True, pos + 1
        else:
            return False, -1

    def next(self) -> str:
        result = "".join(map(lambda x: self._chars[x], self._stack))

        while self._stack:
            next_pos_exists, next_pos = self._next_char(self._stack[-1])

            if next_pos_exists:
                self._stack[-1] = next_pos
                if len(self._stack) == self._length:
                    break
                self._stack.append(next_pos)
            else:
                self._stack.pop()

        return result

    def hasNext(self) -> bool:
        return len(self._stack) > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class CombinationIteratorFirst:

    def __init__(self, characters: str, combinationLength: int):
        self._stack = [0]
        self._comb_len = combinationLength
        self._chars = characters

    def next(self) -> str:
        while self._stack:
            if self._stack[-1] < len(self._chars):
                if len(self._stack) == self._comb_len:
                    result = ''.join(map(lambda x: self._chars[x], self._stack))
                    self._stack[-1] += 1
                    return result
                else:
                    self._stack.append(self._stack[-1] + 1)
            else:
                self._stack.pop()
                if self._stack:
                    self._stack[-1] += 1

    def hasNext(self) -> bool:
        return not (
            len(self._stack) == self._comb_len and \
            self._stack[0] >= len(self._chars) - self._comb_len
        )


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
