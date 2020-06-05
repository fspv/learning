import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self._partial = []
        partial_sum = 0
        for num in w:
            partial_sum += num
            self._partial.append(partial_sum)

    @property
    def _total(self):
        return self._partial[-1]

    def pickIndex(self) -> int:
        return bisect.bisect_left(self._partial, random.randint(1, self._total))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
