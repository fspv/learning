class Reflection:
    def __init__(self, p: int, q: int) -> None:
        self._p = p
        self._q = q

    def _gcd(self, p: int, q: int) -> int:
        while q > 0:
            p, q = q, p % q

        return p

    def _lcm(self, p: int, q: int) -> int:
        return abs(p * q) / self._gcd(p, q)

    def find_detector(self) -> int:
        lcm = self._lcm(self._p, self._q)
        P, Q = lcm // self._p, lcm // self._q

        if P % 2 == 0:
            if Q % 2 == 0:
                raise RuntimeError("Wrong input, ray get back")
            else:
                return 0
        else:
            if Q % 2 == 0:
                return 2
            else:
                return 1


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        obj = Reflection(p, q)

        return obj.find_detector()
