class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
            return

        pre_range = None
        post_range = None
        range_begin = None
        range_end = None

        prev_node = None
        pos = 1
        node = head

        while node:
            node_next = node.next

            if m <= pos <= n:
                range_begin = node if not range_begin else range_begin
                range_end = node
                post_range = node.next

                node.next = prev_node
            else:
                pre_range = node if not post_range else pre_range

            prev_node = node
            node = node_next
            pos += 1

        if range_begin:
            range_begin.next = post_range

        if pre_range:
            pre_range.next = range_end

        if range_begin == head:
            head = range_end

        return head
