# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        list_repr = []
        list_node = self

        while list_node != None:
            list_repr.append(str(list_node.val))
            list_node = list_node.next

        return " -> ".join(list_repr)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class SolutionIter(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        list_node_prev = None
        result = None

        while not (l1 is None and l2 is None):
            try:
                if l1.val > l2.val:
                    add_node = l2
                    l2 = l2.next
                else:
                    add_node = l1
                    l1 = l1.next
            except AttributeError:
                if l1 is None:
                    add_node = l2
                    l2 = l2.next
                elif l2 is None:
                    add_node = l1
                    l1 = l1.next

            try:
                list_node_prev.next = add_node
                list_node_prev = list_node_prev.next
            except AttributeError:
                result = add_node
                list_node_prev = result

        return result


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

solution = Solution()
assert solution.mergeTwoLists(l1, l2).__repr__() == '1 -> 1 -> 2 -> 3 -> 4 -> 4'
