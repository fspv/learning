import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self._head = head


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        length = 0
        node = self._head

        selected = -1

        while node:
            length += 1

            if random.randint(1, length) == 1:
                selected = node.val

            node = node.next

        return selected


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
