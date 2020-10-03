from typing import List, Mapping, Set, Deque
from collections import defaultdict, deque


class RateLimiterTokenBucket:
    def __init__(self, period: float, limit: float) -> None:
        self._tokens = limit
        self._rate = period + 1.0
        self._limit = limit
        self._last_access_ts = 0.0

    def _update_tokens(self, access_ts: float) -> None:
        new_tokens = self._tokens

        new_tokens += (access_ts - self._last_access_ts) / self._rate

        self._tokens = min(self._limit, new_tokens)
        self._last_access_ts = access_ts

    def access(self, access_ts: float, tokens: float = 1.0) -> bool:
        self._update_tokens(access_ts)

        if self._tokens > tokens:
            self._tokens -= tokens
            return True
        else:
            return False


class RateLimiter:
    def __init__(self, period: float, limit: int) -> None:
        self._period = period
        self._limit = limit
        self._queue: Deque[float] = deque(maxlen=limit)

    def access(self, access_ts: float) -> bool:
        result = True
        if (
            len(self._queue) == self._limit
            and self._queue[0] >= access_ts - self._period
        ):
            result = False

        self._queue.append(access_ts)
        return result


def human_time_to_timestamp(human_time: str) -> float:
    hours, minutes = tuple(map(float, human_time.split(":")))

    return hours * 60 * 60 + minutes * 60


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ALERT_LIMIT_PERIOD = 3600.0
        ALERT_LIMIT = 2

        employee_limiter: Mapping[str, RateLimiter] = defaultdict(
            lambda: RateLimiter(ALERT_LIMIT_PERIOD, ALERT_LIMIT)
        )

        result_set: Set[str] = set()

        for employee_name, human_time in sorted(zip(keyName, keyTime)):
            timestamp = human_time_to_timestamp(human_time)

            rate_limiter = employee_limiter[employee_name]

            if not rate_limiter.access(timestamp):
                result_set.add(employee_name)

        return list(sorted(result_set))
