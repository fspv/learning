from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        end = 0

        avg_wait_time = 0.0
        customers_served = 0

        for arrival, time in customers:
            end = max(arrival, end) + time
            avg_wait_time = avg_wait_time * customers_served / (
                customers_served + 1
            ) + (end - arrival) / (customers_served + 1)
            customers_served += 1

        return avg_wait_time
