from collections import deque

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        result  = 0

        before_sum = 0
        after_sum = sum(
            [c for m, c in enumerate(customers) if grumpy[m] == 0]
        )
        cur = deque()
        cur_sum = 0

        for minute, customer in enumerate(customers):
            cur.append((minute, customer))
            cur_sum += customer

            if grumpy[minute] == 0:
                after_sum -= customer

            if len(cur) > X:
                first_minute, first_customer = cur.popleft()
                cur_sum -= first_customer
                if grumpy[first_minute] == 0:
                    before_sum += first_customer

            result = max(result, before_sum + cur_sum + after_sum)

        return result
