import unittest

class BinaryTree(object):
    def __init__(self, array):
        self.array = array

    def _left(self, pos):
        return 2 * pos + 1

    def _right(self, pos):
        return 2 * pos + 2

    def _parent(self, pos):
        return int((pos - 1) / 2)

    def inorder_tree_walk(self, pos=0):
        result = []
        if pos < len(self.array) and self.array[pos] != None:
            result += self.inorder_tree_walk(self._left(pos))
            result += [self.array[pos]]
            result += self.inorder_tree_walk(self._right(pos))

        return result

    def inorder_tree_walk_nonrecursive_stack(self):
        stack = []
        pos = 0
        result = []

        while True:
            while pos is not None and \
                  pos < len(self.array) and \
                  self.array[pos] is not None:
                stack.append(pos)
                pos = self._left(pos)

            if not stack:
                break

            pos = stack.pop()
            result.append(self.array[pos])

            if self._right(pos) < len(self.array) and \
                self.array[self._right(pos)] is not None:
                pos = self._right(pos)
            else:
                pos = None

        return result

    def inorder_tree_walk_nonrecursive_two_pointers(self):
        if not len(self.array):
            return []

        result = []

        pos = 0
        leftdone = False

        while True:
            while not leftdone and \
                  self._left(pos) < len(self.array) and \
                  self.array[self._left(pos)] is not None:
                pos = self._left(pos)

            result.append(self.array[pos])
            leftdone = True

            if self._right(pos) < len(self.array) and \
                  self.array[self._right(pos)] is not None:
                pos = self._right(pos)
                leftdone = False
            else:
                while self._right(self._parent(pos)) == pos and pos != 0:
                    pos = self._parent(pos)

                if pos == 0:
                    break

                pos = self._parent(pos)

                leftdone = True

        return result


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree_inorder_tree_walk(self):
        binary_tree = BinaryTree([])
        self.assertEqual(
            binary_tree.inorder_tree_walk(),
            []
        )

        binary_tree = BinaryTree([0])
        self.assertEqual(
            binary_tree.inorder_tree_walk(),
            [0]
        )

        binary_tree = BinaryTree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(
            binary_tree.inorder_tree_walk(),
            [1, 3, 5, 6, 7, 10, 13, 15, 18]
        )

    def test_binary_tree_inorder_tree_walk_nonrecursive_stack(self):
        binary_tree = BinaryTree([])
        self.assertEqual(
            binary_tree.inorder_tree_walk_nonrecursive_stack(),
            []
        )

        binary_tree = BinaryTree([0])
        self.assertEqual(
            binary_tree.inorder_tree_walk_nonrecursive_stack(),
            [0]
        )

        binary_tree = BinaryTree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(
            binary_tree.inorder_tree_walk_nonrecursive_stack(),
            [1, 3, 5, 6, 7, 10, 13, 15, 18]
        )

    def test_binary_tree_inorder_tree_walk_nonrecursive_two_pointers(self):
        binary_tree = BinaryTree([])
        self.assertEqual(
            binary_tree.inorder_tree_walk_nonrecursive_two_pointers(),
            []
        )

        binary_tree = BinaryTree([0])
        self.assertEqual(
            binary_tree.inorder_tree_walk_nonrecursive_two_pointers(),
            [0]
        )

        binary_tree = BinaryTree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(
            binary_tree.inorder_tree_walk_nonrecursive_two_pointers(),
            [1, 3, 5, 6, 7, 10, 13, 15, 18]
        )


if __name__ == "__main__":
    unittest.main()
