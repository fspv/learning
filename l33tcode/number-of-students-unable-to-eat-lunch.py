from collections import deque
from typing import List, Deque, Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count: Counter[int] = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break
            count[sandwich] -= 1

        return sum(count.values())
