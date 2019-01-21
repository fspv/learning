import unittest

class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self._length = k
        self._queue = [None] * self._length
        self._head = None
        self._tail = None

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self._tail = 0
            self._head = 0
        else:
            self._tail = (self._tail + 1) % self._length

        self._queue[self._tail] = value

        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        if self._tail == self._head:
            self._tail = None
            self._head = None
        else:
            self._head = (self._head + 1) % self._length

        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self._queue[self._head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self._queue[self._tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self._head is None and self._tail is None

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return False \
            if self.isEmpty() else self._head == (self._tail + 1) % self._length

class TestMyCircularQueue(unittest.TestCase):
    def setUp(self):
        self.queue = MyCircularQueue(3)

    def test_empty(self):
        self.assertFalse(self.queue.deQueue())
        self.assertEqual(self.queue.Front(), -1)
        self.assertEqual(self.queue.Rear(), -1)
        self.assertFalse(self.queue.isFull())
        self.assertTrue(self.queue.isEmpty())

    def test_1(self):
        self.assertTrue(self.queue.enQueue(1))
        self.assertEqual(self.queue.Rear(), 1)
        self.assertEqual(self.queue.Front(), 1)
        self.assertFalse(self.queue.isFull())
        self.assertFalse(self.queue.isEmpty())

        self.assertTrue(self.queue.enQueue(2))
        self.assertEqual(self.queue.Front(), 1)
        self.assertEqual(self.queue.Rear(), 2)
        self.assertFalse(self.queue.isFull())
        self.assertFalse(self.queue.isEmpty())

        self.assertTrue(self.queue.enQueue(3))
        self.assertEqual(self.queue.Front(), 1)
        self.assertEqual(self.queue.Rear(), 3)
        self.assertTrue(self.queue.isFull())
        self.assertFalse(self.queue.isEmpty())

        self.assertFalse(self.queue.enQueue(4))
        self.assertEqual(self.queue.Front(), 1)
        self.assertEqual(self.queue.Rear(), 3)
        self.assertTrue(self.queue.isFull())
        self.assertFalse(self.queue.isEmpty())

        self.assertTrue(self.queue.deQueue())
        self.assertEqual(self.queue.Front(), 2)
        self.assertEqual(self.queue.Rear(), 3)
        self.assertFalse(self.queue.isFull())
        self.assertFalse(self.queue.isEmpty())

        self.assertTrue(self.queue.deQueue())
        self.assertEqual(self.queue.Front(), 3)
        self.assertEqual(self.queue.Rear(), 3)
        self.assertFalse(self.queue.isFull())
        self.assertFalse(self.queue.isEmpty())

        self.assertTrue(self.queue.deQueue())
        self.assertEqual(self.queue.Front(), -1)
        self.assertEqual(self.queue.Rear(), -1)
        self.assertFalse(self.queue.isFull())
        self.assertTrue(self.queue.isEmpty())

unittest.main()
