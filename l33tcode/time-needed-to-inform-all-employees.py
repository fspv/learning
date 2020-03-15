class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        result = 0

        dp = [0] * n

        for employee in range(n):
            cur_time = 0
            while employee != headID:
                cur_time += informTime[manager[employee]]
                if cur_time > dp[manager[employee]]:
                    dp[manager[employee]] = cur_time
                    employee = manager[employee]
                else:
                    break

            result = max(result, cur_time)

        return result
