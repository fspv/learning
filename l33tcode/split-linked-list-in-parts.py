class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        def calculate_length(root):
            if root is None:
                return 0

            length = 1
            while root.next:
                length += 1
                root = root.next

            return length

        length = calculate_length(root)
        result = [None for _ in range(k)]

        remain = length % k
        prev = None

        for result_cell in range(k):
            result[result_cell] = root
            for _ in range(length // k):
                if root.next:
                    prev = root
                    root = root.next
                else:
                    return result

            if remain == 0:
                if prev:
                    prev.next = None
                continue

            remain -= 1
            if root.next:
                prev = root
                root = root.next
            else:
                return result

            prev.next = None

        return result


# TODO: Tests are broken
class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.splitListToParts(None, 5) == [[],[],[],[],[]]

    def test_one_elem(self):
        assert self.sol.splitListToParts(ListNode(1), 5) == [[1],[],[],[],[]]

    def test_one(self):
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        assert self.sol.splitListToParts(l, 5) == [[1],[2],[3],[],[]]

    def test_two(self):
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        l.next.next.next = ListNode(4)
        l.next.next.next.next = ListNode(5)
        l.next.next.next.next.next = ListNode(6)
        l.next.next.next.next.next.next = ListNode(7)
        l.next.next.next.next.next.next.next = ListNode(8)
        l.next.next.next.next.next.next.next.next = ListNode(9)
        l.next.next.next.next.next.next.next.next.next = ListNode(10)
        assert self.sol.splitListToParts(l, 3) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
