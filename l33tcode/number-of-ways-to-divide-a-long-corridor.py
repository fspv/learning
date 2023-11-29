MOD = 10 ** 9 + 7


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count("S") % 2 or corridor.count("S") == 0:
            return 0

        ways = 1
        seats = 0
        plants = 0

        for pos in range(corridor.index("S"), len(corridor)):
            char = corridor[pos]
            if char == "S":
                seats += 1
                seats %= 2

                if seats == 1:
                    ways *= plants + 1
                    ways %= MOD

                plants = 0
            else:
                plants += 1

        return ways
