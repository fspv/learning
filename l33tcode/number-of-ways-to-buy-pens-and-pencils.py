class Solution:
    def waysToBuyPensPencils(self, total: int, cost_pen: int, cost_pencil: int) -> int:
        count = 0

        for pens in range(total // cost_pen + 1):
            left = total - pens * cost_pen

            count += 1

            if left > 0:
                count += left // cost_pencil

        return count
