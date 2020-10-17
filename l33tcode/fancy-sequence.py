class Fancy:
    def __init__(self):
        self._container = []
        self._multipliers = [1]
        self._additions = [0]
        self._mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self._container.append(val)
        self._multipliers.append(self._multipliers[-1])
        self._additions.append(self._additions[-1])

    def addAll(self, inc: int) -> None:
        self._additions[-1] += inc

    def multAll(self, m: int) -> None:
        self._additions[-1] *= m
        self._multipliers[-1] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self._container):
            return -1

        tmp = self._multipliers[-1] // self._multipliers[idx]

        value = self._container[idx]
        value *= tmp
        value %= self._mod
        value += self._additions[-1] - (self._additions[idx] * tmp) % self._mod

        return value % self._mod


class FancyBruteForce:
    def __init__(self):
        self._container = []
        self._ops = []
        self._mod = 10 ** 9 + 7
        self._first_op = []

    def append(self, val: int) -> None:
        self._container.append(val)
        self._first_op.append(len(self._ops) - 1)

    def addAll(self, inc: int) -> None:
        new_op = [inc, len(self._container) - 1, "add"]

        if (
            self._ops
            and self._ops[-1][2] == "add"
            and self._ops[-1][1] == len(self._container) - 1
        ):
            old_inc, _, _ = self._ops.pop()
            new_op[0] += old_inc

        self._ops.append(new_op)

    def multAll(self, m: int) -> None:
        new_op = [m, len(self._container) - 1, "mul"]

        if (
            self._ops
            and self._ops[-1][2] == "mul"
            and self._ops[-1][1] == len(self._container) - 1
        ):
            old_m, _, _ = self._ops.pop()
            new_op[0] *= old_m

        self._ops.append(new_op)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self._container):
            return -1

        value = self._container[idx]

        pos = max(0, self._first_op[idx])
        while pos < len(self._ops):
            num, op_pos, op = self._ops[pos]
            if op_pos >= idx:
                if op == "mul":
                    value *= num
                else:
                    value += num

            pos += 1

        return value % self._mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
