import heapq

class Solution:
    def coinChange(self, coins, amount):
        dp = [-1] * amount + [0]

        left = amount

        while left > 0:
            if dp[left] == -1:
                left -= 1
                continue

            for coin in coins:
                if left >= coin:
                    if dp[left - coin] > 0:
                        dp[left - coin] = min(dp[left] + 1, dp[left - coin])
                    else:
                        dp[left - coin] = dp[left] + 1

            left -= 1

        return dp[0]

    def coinChangeTry2(self, coins, amount):
        dp = [0] + [-1] * amount
        dp_nonempty = [0]
        dp_nonempty_set = set([0])

        while len(dp_nonempty):
            total = heapq.heappop(dp_nonempty)

            for coin in coins:
                total_next = total + coin
                if total_next <= amount:
                    if dp[total_next] > 0:
                        dp[total_next] = min(dp[total] + 1, dp[total_next])
                    else:
                        dp[total_next] = dp[total] + 1
                    if total_next not in dp_nonempty_set:
                        heapq.heappush(dp_nonempty, total_next)
                        dp_nonempty_set.add(total_next)

        return dp[amount]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty1(self):
        assert self.sol.coinChange([], 11) == -1

    def test_empty2(self):
        assert self.sol.coinChange([], 0) == 0

    def test_custom1(self):
        assert self.sol.coinChange([1], 1) == 1

    def test_custom2(self):
        assert self.sol.coinChange([2], 3) == -1

    def test_custom3(self):
        assert self.sol.coinChange([1, 2, 5], 11) == 3
