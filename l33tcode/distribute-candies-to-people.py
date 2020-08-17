import math
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = []
        candy_piles = math.sqrt(2 * candies + 0.25) - 0.5
        candies_left = candies

        for pos in range(1, num_people + 1):
            candy_piles_given = candy_piles // num_people

            candies_given = int(
                (2 * (pos) + (candy_piles_given - 1) * num_people)
                * candy_piles_given
                / 2
            )
            candies_left -= candies_given
            result.append(candies_given)

        for pos in range(1, num_people + 1):
            candies_given = min(
                candies_left, int((candy_piles // num_people) * num_people + pos)
            )
            if candies_left > 0:
                result[pos - 1] += candies_given

            candies_left -= candies_given

        return result
