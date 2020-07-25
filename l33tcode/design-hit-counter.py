from collections import deque


class TimestampCounter:
    def __init__(self, timestamp, count):
        self.timestamp = timestamp
        self.count = count

    def __repr__(self):
        return str(f"TimestampCounter({self.timestamp}, {self.count})")


def current_time(timestamp):
    return timestamp  # FIXME: should be time.time() in real app


class HitCounter:
    COUNTER_TIME_WINDOW = 300  # 5 minutes

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque(maxlen=self.COUNTER_TIME_WINDOW)
        self.count = 0
        self.timestamp_counters = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.timestamp_counters:
            timestamp_counter = self.timestamp_counters[timestamp]
            timestamp_counter.count += 1
            self.count += 1
        elif timestamp > current_time(timestamp) - self.COUNTER_TIME_WINDOW:
            # If we haven't received an event from the past
            timestamp_counter = TimestampCounter(timestamp, 1)
            self.queue.append(timestamp_counter)
            self.timestamp_counters[timestamp] = timestamp_counter
            self.count += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while (
            self.queue
            and self.queue[0].timestamp <= current_time(timestamp) - self.COUNTER_TIME_WINDOW
        ):
            timestamp_counter = self.queue.popleft()
            del self.timestamp_counters[timestamp_counter.timestamp]
            self.count -= timestamp_counter.count

        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
