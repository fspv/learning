# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def print_n_nodes_reversed(node, n):
            nodes = [node]

            for _ in range(n - 1):
                if node := node.getNext():
                    nodes.append(node)
                else:
                    break

            for node in reversed(nodes):
                node.printValue()

        def get_each_n_node(node, n):
            nodes = [node]
            count = 0

            while node := node.getNext():
                count += 1
                if count % n == 0:
                    nodes.append(node)

            return nodes

        def get_list_lenght(node):
            count = 0

            while node := node.getNext():
                count += 1

            return count

        # Value 10 here is chosen arbitrarily. It could be lg(n) for example
        # to make space complexity non-linear
        n = (get_list_lenght(head) // 10) or 1

        for node in reversed(get_each_n_node(head, n)):
            print_n_nodes_reversed(node, n)
