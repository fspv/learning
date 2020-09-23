class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = 0
        min_pos, min_val = 0, float("+inf")
        for pos in range(len(gas)):
            if min_val > left:
                min_pos = pos
                min_val = left

            left += gas[pos] - cost[pos]

        if left >= 0:
            return min_pos

        return -1

    def canCompleteCircuitBruteForce(self, gas: List[int], cost: List[int]) -> int:
        def dfs(pos: int, start_pos: int, gas_left: int) -> bool:
            if gas_left < 0:
                return False

            if pos == start_pos:
                return True

            return dfs((pos + 1) % len(gas), start_pos, gas_left + gas[pos] - cost[pos])

        for pos in range(len(gas)):
            if dfs((pos + 1) % len(gas), pos, gas[pos] - cost[pos]):
                return pos

        return -1
