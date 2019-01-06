import unittest

class MaxHeap(object):
    def _left(self, pos):
        return 2 * pos + 1

    def _right(self, pos):
        return 2 * pos + 2

    def _parent(self, pos):
        return int((pos - 1) / 2)

    @property
    def _largest(self):
        return 0

    def build_max_heap(self, array):
        self.array = array
        self._heap_size = len(self.array)

        for pos in range(int(self._heap_size / 2) - 1, -1, -1):
            self._max_heapify(pos)

    def sort(self):
        for _ in range(self._heap_size - 1):
            self.array[self._largest], self.array[self._heap_size - 1] = \
                self.array[self._heap_size - 1], self.array[self._largest]

            self._heap_size -= 1

            self._max_heapify(0)

    def _max_heapify(self, pos):
        left = self._left(pos)
        right = self._right(pos)
        largest = pos

        if left < self._heap_size and self.array[left] > self.array[pos]:
            largest = left

        if right < self._heap_size and self.array[right] > self.array[largest]:
            largest = right

        if largest == pos:
            return

        self.array[largest], self.array[pos] = \
            self.array[pos], self.array[largest]

        self._max_heapify(largest)


class MaxHeapTests(unittest.TestCase):
    def test_max_heap(self):
        max_heap = MaxHeap()
        max_heap.build_max_heap([])
        self.assertEqual(max_heap.array, [])
        max_heap.sort()
        self.assertEqual(max_heap.array, [])

        max_heap = MaxHeap()
        max_heap.build_max_heap([0])
        self.assertEqual(max_heap.array, [0])
        max_heap.sort()
        self.assertEqual(max_heap.array, [0])

        max_heap = MaxHeap()
        max_heap.build_max_heap([3, 2, 1])
        self.assertEqual(max_heap.array, [3, 2, 1])
        max_heap.sort()
        self.assertEqual(max_heap.array, [1, 2, 3])

        max_heap = MaxHeap()
        max_heap.build_max_heap([2, 3, 1])
        self.assertEqual(max_heap.array, [3, 2, 1])
        max_heap.sort()
        self.assertEqual(max_heap.array, [1, 2, 3])

        max_heap = MaxHeap()
        max_heap.build_max_heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(max_heap.array, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        max_heap.sort()
        self.assertEqual(max_heap.array, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])

        max_heap = MaxHeap()
        max_heap.build_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        self.assertEqual(max_heap.array, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        max_heap.sort()
        self.assertEqual(max_heap.array, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])


if __name__ == "__main__":
    unittest.main()
