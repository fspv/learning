class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower_row = [float(poured)]

        for row in range(query_row + 1):
            tower_row_prev = tower_row
            tower_row = [0.0] * (row + 2)
            for col in range(row + 1):
                excess = tower_row_prev[col] - 1
                if excess > 0:
                    tower_row[col] += excess / 2
                    tower_row[col + 1] += excess / 2
                    tower_row_prev[col] = 1

        return tower_row_prev[query_glass]
