from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people) - 1

        boats = len(people)

        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                boats -= 1

            right -= 1


        return boats
