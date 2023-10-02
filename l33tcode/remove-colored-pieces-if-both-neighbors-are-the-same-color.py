class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a = count_b = 0

        for pos in range(1, len(colors) - 1):
            if colors[pos - 1] == colors[pos] == colors[pos + 1]:
                if colors[pos] == "A":
                    count_a += 1
                else:
                    count_b += 1

        return count_a > count_b
