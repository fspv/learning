from collections import deque
from enum import Enum
from typing import Deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        def build_adj_list() -> list[list[int]]:
            adj_list: list[list[int]] = [[] for _ in range(numCourses)]

            for src, dst in prerequisites:
                adj_list[src].append(dst)

            return adj_list

        def build_indegrees(adj_list: list[list[int]]) -> list[int]:
            indegrees = [0] * numCourses

            for dsts in adj_list:
                for dst in dsts:
                    indegrees[dst] += 1

            return indegrees

        adj_list = build_adj_list()
        indegrees = build_indegrees(adj_list)

        queue: Deque[int] = deque()

        for pos, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(pos)

        result: list[int] = []

        while queue:
            pos = queue.popleft()
            result.append(pos)

            for next_pos in adj_list[pos]:
                indegrees[next_pos] -= 1

                if indegrees[next_pos] == 0:
                    queue.append(next_pos)

        if len(result) != numCourses:
            return []

        return list(reversed(result))

    def findOrderDFS(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        class Color(Enum):
            WHITE = 0
            GRAY = 1
            BLACK = 2

        courses_next = [[] for _ in range(numCourses)]
        courses_color = [Color.WHITE for _ in range(numCourses)]

        for prerequisite in prerequisites:
            courses_next[prerequisite[0]].append(prerequisite[1])

        result = []

        def dfs(course: int) -> bool:
            """
            @return False - loop, True - no loop
            """
            if courses_color[course] == Color.GRAY:
                return False

            if courses_color[course] == Color.BLACK:
                return True

            courses_color[course] = Color.GRAY

            for next_course in courses_next[course]:
                if not dfs(next_course):
                    return False

            courses_color[course] = Color.BLACK
            result.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result

    def findOrderStraighforward(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        courses = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])

        taken = set()
        result = []

        def dfs(course: int, path: set[int]) -> bool:
            if course in path:
                return False

            if course in taken:
                return True

            path.add(course)

            for next_course in courses[course]:
                if not dfs(next_course, path):
                    return False

            taken.add(course)
            path.remove(course)

            result.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return []

        return result
