from functools import lru_cache


MAX_PRICE = float("+inf")


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache
        def dfs(day: int) -> int:
            if day == len(days):
                return 0

            result = MAX_PRICE


            for valid_for, cost in zip([1, 7, 30], costs):
                next_day = day + 1
                while next_day < len(days) and (days[next_day] - days[day]) < valid_for:
                    next_day += 1

                result = min(result, dfs(next_day) + cost)

            return result

        return dfs(0)
