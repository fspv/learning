import sys
from functools import lru_cache
from typing import Iterator, List, Tuple, Dict, Optional

dp = {}

for power in range(31):
    # key is the number that we can achieve on this level
    # value is if the current power of 2 is included to the sum for this key
    # or not
    if power == 0:
        dp[power] = {1: True, -1: True, 0: False}
    else:
        dp[power] = {}


def parse_input(lines: Iterator[str]) -> Iterator[Tuple[int, ...]]:
    number_of_tests = int(next(lines))

    for _ in range(number_of_tests):
        yield tuple(map(int, next(lines).split()))


def solution(x: int, y: int) -> Optional[List[str]]:
    current = 1
    current_sum = 1
    max_power = 0
    for power in range(1, 31):
        max_power = power
        current *= 2
        current_sum += current
        if not dp[power]:
            dp[power][current] = True
            for num, included in dp[power - 1].items():
                dp[power][num] = False
                if num - current not in dp[power]:
                    dp[power][num - current] = True
                if num + current not in dp[power]:
                    dp[power][num + current] = True

        if current_sum > abs(x) + abs(y):
            break

    def dfs(
        x: int, y: int, power: int, current: int, dp: Dict[int, Dict[int, bool]]
    ) -> Optional[List[str]]:
        if power == -1  and x == 0 and y == 0:
            return ["O"]

        if power == -1:
            return None

        if x in dp[power] and y in dp[power]:
            if not dp[power][x] and dp[power][y]:
                if (res := dfs(x, y - current, power - 1, int(current / 2), dp)) :
                    return res + ["N"]
                if (res := dfs(x, y + current, power - 1, int(current / 2), dp)) :
                    return res + ["S"]
            elif dp[power][x] and not dp[power][y]:
                if (res := dfs(x - current, y, power - 1, int(current / 2), dp)) :
                    return res + ["E"]
                if (res := dfs(x + current, y, power - 1, int(current / 2), dp)) :
                    return res + ["W"]
            elif not dp[power][x] and not dp[power][y]:
                if (res := dfs(x, y, power - 1, int(current / 2), dp)) :
                    return res
                if (res := dfs(x, y - current, power - 1, int(current / 2), dp)) :
                    return res + ["N"]
                if (res := dfs(x, y + current, power - 1, int(current / 2), dp)) :
                    return res + ["S"]
                if (res := dfs(x - current, y, power - 1, int(current / 2), dp)) :
                    return res + ["E"]
                if (res := dfs(x + current, y, power - 1, int(current / 2), dp)) :
                    return res + ["W"]

        return None

    return dfs(x, y, max_power, current, dp)


def main():
    case = 1
    for x, y in parse_input(sys.stdin):
        directions = solution(x, y)

        if directions:
            print("Case #%s: %s" % (case, "".join(directions[1:])))
        else:
            print("Case #%s: IMPOSSIBLE" % case)

        case += 1


if __name__ == "__main__":
    main()
