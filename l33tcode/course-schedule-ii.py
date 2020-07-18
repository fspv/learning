from enum import Enum


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class Color(Enum):
            WHITE = 0
            GRAY = 1
            BLACK = 2

        courses_next = [[] for _ in range(numCourses)]
        courses_color = [Color.WHITE for _ in range(numCourses)]

        for prerequisite in prerequisites:
            courses_next[prerequisite[0]].append(prerequisite[1])

        result = []

        def dfs(course):
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
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        courses = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])

        taken = set()
        result = []

        def dfs(course, path):
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
