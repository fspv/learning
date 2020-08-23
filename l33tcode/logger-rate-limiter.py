from collections import Counter, deque, defaultdict


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = defaultdict(lambda: -11)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp - self.hashmap[message] >= 10:
            self.hashmap[message] = timestamp
            return True
        else:
            return False


class MessageBucket:
    def __init__(self, timestamp: int):
        self.timestamp = timestamp
        self.messages: Counter = Counter()

    def __repr__(self) -> str:
        return f"MessageBucket({self.timestamp}), messages: {self.messages}"


class Logger2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._message_counter: Counter = Counter()
        self._message_bucket_queue: deque = deque()
        self._keep_timestamps = 10

    def _drop_old_timestamps(self, timestamp: int) -> None:
        while (
            self._message_bucket_queue
            and self._message_bucket_queue[0].timestamp <= timestamp - 10
        ):
            message_bucket = self._message_bucket_queue.popleft()

            for message, count in message_bucket.messages.items():
                self._message_counter[message] -= count

    def _add_new_message_bucket(self, timestamp: int) -> None:
        if (
            not self._message_bucket_queue
            or self._message_bucket_queue[-1].timestamp != timestamp
        ):
            message_bucket = MessageBucket(timestamp)
            self._message_bucket_queue.append(message_bucket)

    def _add_new_message(self, message: str) -> None:
        message_bucket = self._message_bucket_queue[-1]
        message_bucket.messages[message] += 1
        self._message_counter[message] += 1

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        self._drop_old_timestamps(timestamp)

        if self._message_counter[message] == 0:
            self._add_new_message_bucket(timestamp)
            self._add_new_message(message)
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
