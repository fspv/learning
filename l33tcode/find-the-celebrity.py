# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    ...


class Solution:
    def findCelebrity(self, n: int) -> int:
        person_left, person_right = 0, 0

        while person_right < n:
            if person_left == person_right:
                person_right += 1
            elif knows(person_left, person_right):
                person_left += 1
            else:
                person_right += 1

        for person_right in range(n):
            if person_left != person_right and (
                knows(person_left, person_right) or not knows(person_right, person_left)
            ):
                return -1

        return person_left
