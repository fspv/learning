import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]

        seen = {1}
        heap = [1]
        count = 0
        result = 0

        while count < n:
            num = heapq.heappop(heap)
            count += 1
            result = num

            for factor in factors:
                new_num = num * factor

                if new_num not in seen:
                    heapq.heappush(heap, new_num)

                seen.add(new_num)

        return result
