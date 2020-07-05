# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def turn_left(direction, robot):
            robot.turnLeft()
            return direction[1], -direction[0]

        def turn_right(direction, robot):
            robot.turnRight()
            return -direction[1], direction[0]

        def dfs(robot, visited, row, col, direction):
            visited.add((row, col))
            robot.clean()
            for _ in range(4):
                next_row, next_col = row + direction[0], col + direction[1]
                if (next_row, next_col) not in visited and robot.move():
                    direction = dfs(robot, visited, next_row, next_col, direction)
                    direction = turn_left(direction, robot)
                else:
                    direction = turn_right(direction, robot)

            direction = turn_left(direction, robot)
            direction = turn_left(direction, robot)
            robot.move()

            return direction

        dfs(robot, set(), 0, 0, (1, 0))
