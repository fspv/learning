from functools import cache

MOD = 10**9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        def dp(pickups: int, deliveries: int) -> int:
            if pickups < 0 or deliveries < 0:
                # This branch is not possible
                return 0

            if pickups == 0 and deliveries == 0:
                # Delivered everything, done
                return 1

            # Do a pickup of any of not picked up orders
            count = pickups * dp(pickups - 1, deliveries + 1)

            # Delivery any of the picked up orders
            count += deliveries * dp(pickups, deliveries - 1)

            return count % MOD

        return dp(n, 0)
