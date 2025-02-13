from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    var: int
    next: ListNode | None

    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        list_repr = []
        list_node = self

        while list_node != None:
            list_repr.append(str(list_node.val))
            list_node = list_node.next

        return " -> ".join(list_repr)


class Solution(object):
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        head = ListNode(0)
        prev = head

        while prev and (l1 or l2):
            if l1 and l2:
                if l1.val < l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
            elif l1:
                prev.next = l1
                l1 = l1.next
            elif l2:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        return head.next


class SolutionRecursive:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
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
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        list_node_prev = None
        result = None

        while not (l1 is None and l2 is None):
            try:
                if l1.val > l2.val:  # type: ignore
                    add_node = l2
                    l2 = l2.next  # type: ignore
                else:
                    add_node = l1
                    l1 = l1.next  # type: ignore
            except AttributeError:
                if l1 is None:
                    add_node = l2
                    l2 = l2.next  # type: ignore
                elif l2 is None:
                    add_node = l1
                    l1 = l1.next

            try:
                list_node_prev.next = add_node  # type: ignore
                list_node_prev = list_node_prev.next  # type: ignore
            except AttributeError:
                result = add_node  # type: ignore
                list_node_prev = result

        return result


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

solution = Solution()
assert solution.mergeTwoLists(l1, l2).__repr__() == "1 -> 1 -> 2 -> 3 -> 4 -> 4"
