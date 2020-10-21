from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []

        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < -asteroid:
                        stack.pop()
                    elif stack[-1] == -asteroid:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)

        return stack
