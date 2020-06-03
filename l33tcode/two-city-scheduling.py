class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        return sum(c[n // (len(costs) // 2)] for n, c in enumerate(costs))
