from dataclasses import dataclass
import bisect

@dataclass
class Value:
    value: int
    snapshot_id: int

    def __eq__(self, other) -> bool:
        return self.snapshot_id == other.snapshot_id

    def __lt__(self, other) -> bool:
        return self.snapshot_id < other.snapshot_id

class SnapshotArray:
    _values: list[list[Value]]
    _snapshot_id: int

    def __init__(self, length: int):
        self._values = [[Value(0, 0)] for _ in range(length)]
        self._snapshot_id = 0

    def set(self, index: int, val: int) -> None:
        if self._values[index][-1].snapshot_id == self._snapshot_id:
            self._values[index][-1] = Value(val, self._snapshot_id)
        else:
            self._values[index].append(Value(val, self._snapshot_id))

    def snap(self) -> int:
        self._snapshot_id += 1

        return self._snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect.bisect_right(self._values[index], Value(0, snap_id))

        return self._values[index][pos-1].value
