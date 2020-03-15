from collections import Counter
from typing import List


class LinkedListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class BinaryTreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.elements = Counter()  # number of people to the left by height
        self.elements_total = 0  # total number of people to the left
        self.person = None


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def construct_binary_tree(node, left_interval, right_interval):
            left, right = left_interval
            if left < right:
                middle = (left + right) // 2

                node.left = BinaryTreeNode(middle)
                construct_binary_tree(node.left, (left, middle), (middle + 1, right))

            left, right = right_interval
            if left < right:
                middle = (left + right) // 2

                node.right = BinaryTreeNode(middle)
                construct_binary_tree(node.right, (left, middle), (middle + 1, right))

        def tree_insert(node, person, less):
            equal_or_missing = node.elements[person[0]] + (
                node.val - node.elements_total - less
            )
            if equal_or_missing > person[1]:
                node.elements[person[0]] += 1
                node.elements_total += 1
                tree_insert(node.left, person, less)
            elif equal_or_missing < person[1]:
                tree_insert(
                    node.right,
                    person,
                    node.val
                    - equal_or_missing
                    + (1 if node.person and node.person[0] != person[0] else 0),
                )
            else:
                if node.person:
                    tree_insert(node.right, person, node.val - equal_or_missing + 1)
                else:
                    node.person = person

        def inorder_walk(node):
            if node.left:
                yield from inorder_walk(node.left)
            yield node.person
            if node.right:
                yield from inorder_walk(node.right)

        if not people:
            return []

        middle = len(people) // 2
        root = BinaryTreeNode(middle)

        construct_binary_tree(root, (0, middle), (middle + 1, len(people)))

        people.sort()

        for person in people:
            tree_insert(root, person, 0)

        return list(inorder_walk(root))

    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()

        result = [None] * len(people)

        for person in people:
            equal_or_missing = 0
            for pos in range(len(result)):
                if result[pos] is None and equal_or_missing == person[1]:
                    result[pos] = person
                    break
                if result[pos] is None or result[pos][0] == person[0]:
                    equal_or_missing += 1

        return result

    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[1])
        linked_list = LinkedListNode(None)

        for person in people:
            count = 0
            node = linked_list

            while node.next is not None:
                if node.next.val[0] >= person[0]:
                    count += 1

                if count <= person[1]:
                    node = node.next
                else:
                    break

            next_node = node.next
            node.next = LinkedListNode(person)
            node.next.next = next_node

        result = []

        node = linked_list.next
        while node:
            result.append(node.val)
            node = node.next

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.reconstructQueue([]) == []

    def test_case1(self):
        assert self.sol.reconstructQueue(
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        ) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

    def test_case2(self):
        assert self.sol.reconstructQueue(
            [
                [0, 0],
                [6, 2],
                [5, 5],
                [4, 3],
                [5, 2],
                [1, 1],
                [6, 0],
                [6, 3],
                [7, 0],
                [5, 1],
            ]
        ) == [
            [0, 0],
            [6, 0],
            [1, 1],
            [5, 1],
            [5, 2],
            [4, 3],
            [7, 0],
            [6, 2],
            [5, 5],
            [6, 3],
        ]
