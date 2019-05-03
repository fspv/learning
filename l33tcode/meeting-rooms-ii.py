import heapq
from collections import deque


class Solution:
    def minMeetingRooms(self, intervals):
        rooms = []
        result = 0

        for interval in sorted(intervals):
            if rooms and rooms[0] <= interval[0]:
                while rooms and rooms[0] <= interval[0]:
                    heapq.heappop(rooms)

            heapq.heappush(rooms, interval[1])

            result = max(result, len(rooms))

        return result


    def minMeetingRoomsOptimizedBruteforce(self, intervals):
        # Runs in ~ N * number of rooms time in average case
        queue = deque()
        result = 0

        for interval in sorted(intervals):
            while queue:
                if queue[0][1] <= interval[0]:
                    queue.popleft()
                elif queue[-1][1] <= interval[0]:
                    queue.pop()
                else:
                    break
            queue.append(interval)
            result = max(
                result,
                len(list(filter(lambda x: x[1] > interval[0], queue)))
            )

        return result
