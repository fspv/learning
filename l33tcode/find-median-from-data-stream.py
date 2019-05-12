import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_left = []
        self.heap_right = []

    def addNum(self, num: int) -> None:
        if len(self.heap_left) == len(self.heap_right):
            heapq.heappush(self.heap_left, - num)
        else:
            heapq.heappush(self.heap_right, num)

        if not len(self.heap_right):
            return

        left = - self.heap_left[0]
        right = self.heap_right[0]

        if left > right:
            heapq.heapreplace(self.heap_left, - right)
            heapq.heapreplace(self.heap_right, left)

    def findMedian(self) -> float:
        if len(self.heap_left) == len(self.heap_right):
            return (- self.heap_left[0] + self.heap_right[0]) / 2.0
        else:
            return - self.heap_left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
