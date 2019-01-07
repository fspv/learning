import unittest

class BinaryTreeArray(object):
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

    def preorder_tree_walk(self, pos=0):
        # Not tested
        result = []
        if pos < len(self.array) and self.array[pos] != None:
            result += [self.array[pos]]
            result += self.preorder_tree_walk(self._left(pos))
            result += self.preorder_tree_walk(self._right(pos))

        return result

    def postorder_tree_walk(self, pos=0):
        # Not tested
        result = []
        if pos < len(self.array) and self.array[pos] != None:
            result += self.postorder_tree_walk(self._left(pos))
            result += self.postorder_tree_walk(self._right(pos))
            result += [self.array[pos]]

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


class BinaryTreeException(object):
    pass


class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree(object):
    def __init__(self, array):
        self.root = None

        for val in array:
            if val is not None:
                node = BinaryTreeNode(val)
                self.insert(node)
                self.check_ri() # for test purposes

    def inorder_walk(self, subtree_node=None):
        if subtree_node is None:
            if self.root is None:
                return []
            subtree_node = self.root

        result = []

        if subtree_node.left is not None:
            result += self.inorder_walk(subtree_node.left)

        result += [subtree_node.val]

        if subtree_node.right is not None:
            result += self.inorder_walk(subtree_node.right)

        return result

    def check_ri(self, subtree_node=None):
        """Check representation invariant"""
        if subtree_node is None:
            subtree_node = self.root

        if subtree_node.left is not None:
            left_val = self.check_ri(subtree_node.left)
            if left_val > subtree_node.val:
                raise BinaryTreeException

        if subtree_node.right is not None:
            right_val = self.check_ri(subtree_node.right)
            if right_val < subtree_node.val:
                raise BinaryTreeException

        return subtree_node.val

    def search(self, val):
        prev = None
        current = self.root

        while current is not None:
            if current.val < val:
                prev = current
                current = current.right
            elif current.val > val:
                prev = current
                current = current.left
            else:
                return current

        return current

    def min(self, subtree_root=None):
        current = self.root if subtree_root is None else subtree_root
        result = current

        while current is not None:
            result = current
            current = current.left

        return result

    def max(self, subtree_root=None):
        current = self.root if subtree_root is None else subtree_root
        result = current

        while current is not None:
            result = current
            current = current.right

        return result

    def min_recursive(self, subtree_root=None):
        if self.root is None:
            return

        subtree_root = self.root if subtree_root is None else subtree_root

        if subtree_root.left is not None:
            return self.min_recursive(subtree_root.left)
        else:
            return subtree_root

    def max_recursive(self, subtree_root=None):
        if self.root is None:
            return

        subtree_root = self.root if subtree_root is None else subtree_root

        if subtree_root.right is not None:
            return self.max_recursive(subtree_root.right)
        else:
            return subtree_root

    def successor(self, node):
        if node.right is not None:
            return self.min(node.right)
        else:
            prev = node
            current = prev.parent

            while current is not None and current.right == prev:
                prev = current
                current = prev.parent

            return current

    def predecessor(self, node):
        if node.left is not None:
            return self.max(node.left)
        elif node.parent is not None and node.parent.right == node:
            return node.parent
        else:
            prev = node
            current = prev.parent

            while current is not None and current.left == prev:
                prev = current
                current = prev.parent

            return current

    def insert(self, node):

        # Process situation when tree is empty
        if self.root is None:
            self.root = node
            return

        # Go all the way down to find a place for new node
        prev = None
        current = self.root

        while current is not None:
            prev = current
            if current.val < node.val:
                current = current.right
            elif current.val > node.val:
                current = current.left
            else:
                return

        # Insert the node to the place we found
        if prev.val < node.val:
            prev.right = node
            node.parent = prev
        elif prev.val > node.val:
            prev.left = node
            node.parent = prev

    def delete(self, node):
        # not tested
        if node.left is None and node.right is None:
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = None
                if node.parent.right == node:
                    node.parent.right = None
            else:
                self.root = None
        elif node.left is None:
            node.parent = node.right
        elif node.right is None:
            node.parent = node.left
        else:
            left = node.left
            right = node.right
            parent = node.parent
            node = self.min(node.right)
            node.parent = parent
            node.left = left
            # TODO: handle the situation when node == right (i.e. right
            # element is min element of the right subtree)
            node.right = right


class TemplateBinaryTreeInorderWalk(object):
    def test_binary_tree_inorder_walk_empty(self):
        self.construct_tree([])
        self.assertEqual(
            self.binary_tree_inorder_walk(), []
        )

    def test_binary_tree_inorder_walk_one_element(self):
        self.construct_tree([0])
        self.assertEqual(
            self.binary_tree_inorder_walk(), [0]
        )

    def test_binary_tree_inorder_walk_1(self):
        self.construct_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(
            self.binary_tree_inorder_walk(), [1, 3, 5, 6, 7, 10, 13, 15, 18]
        )


class TestBinaryTreeArrayInorderWalk(
    TemplateBinaryTreeInorderWalk, unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTreeArray(array)

    def binary_tree_inorder_walk(self):
        return self.binary_tree.inorder_tree_walk()


class TestBinaryTreeArrayInorderWalkNonrecursiveStack(
    TemplateBinaryTreeInorderWalk, unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTreeArray(array)

    def binary_tree_inorder_walk(self):
        return self.binary_tree.inorder_tree_walk_nonrecursive_stack()


class TestBinaryTreeArrayInorderWalkNonrecursiveTwoPointers(
    TemplateBinaryTreeInorderWalk, unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTreeArray(array)

    def binary_tree_inorder_walk(self):
        return self.binary_tree.inorder_tree_walk_nonrecursive_two_pointers()


class TestBinaryTreeInorderWalk(
    TemplateBinaryTreeInorderWalk, unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTree(array)

    def binary_tree_inorder_walk(self):
        return self.binary_tree.inorder_walk()


class TemplateBinaryTreeMinMax(object):
    def test_binary_tree_max_empty(self):
        self.construct_tree([])
        self.assertEqual(
            self.binary_tree_max(), None
        )

    def test_binary_tree_max_one_element(self):
        self.construct_tree([0])
        self.assertEqual(
            self.binary_tree_max().val, 0
        )

    def test_binary_tree_max_1(self):
        self.construct_tree([10, 5, 15, 3, 7, 13, 18, 1, 6])
        self.assertEqual(
            self.binary_tree_max().val, 18
        )

    def test_binary_tree_min_empty(self):
        self.construct_tree([])
        self.assertEqual(
            self.binary_tree_min(), None
        )

    def test_binary_tree_min_one_element(self):
        self.construct_tree([0])
        self.assertEqual(
            self.binary_tree_min().val, 0
        )

    def test_binary_tree_min_1(self):
        self.construct_tree([10, 5, 15, 3, 7, 13, 18, 1, 6])
        self.assertEqual(
            self.binary_tree_min().val, 1
        )


class TestBinaryTreeMinMax(
    TemplateBinaryTreeMinMax, unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTree(array)

    def binary_tree_min(self):
        return self.binary_tree.min()

    def binary_tree_max(self):
        return self.binary_tree.max()


class TestBinaryTreeMinMaxRecursive(
    TemplateBinaryTreeMinMax, unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTree(array)

    def binary_tree_min(self):
        return self.binary_tree.min_recursive()

    def binary_tree_max(self):
        return self.binary_tree.max_recursive()


class TestBinaryTreeSuccessorPredecessor(unittest.TestCase):
    def construct_tree(self, array):
        self.binary_tree = BinaryTree(array)

    def test_binary_tree_successor_empty(self):
        self.construct_tree([])
        node = self.binary_tree.search(0)
        self.assertEqual(
            node, None
        )

    def test_binary_tree_successor_one_element(self):
        self.construct_tree([0])
        node = self.binary_tree.search(0)
        self.assertEqual(node.val, 0)
        self.assertEqual(
            self.binary_tree.successor(node), None
        )

    def test_binary_tree_successor_1(self):
        array = [10, 5, 15, 3, 7, 13, 18, 1, 6]
        array_sorted = sorted(array)
        self.construct_tree(array)

        for i in range(len(array_sorted)):
            cur = array_sorted[i]
            succ = array_sorted[i + 1] if i < len(array_sorted) - 1 else None
            node = self.binary_tree.search(cur)
            self.assertEqual(node.val, cur)
            if succ is None:
                self.assertEqual(
                    self.binary_tree.successor(node), succ
                )
            else:
                self.assertEqual(
                    self.binary_tree.successor(node).val, succ
                )

    def test_binary_tree_predecessor_empty(self):
        self.construct_tree([])
        node = self.binary_tree.search(0)
        self.assertEqual(
            node, None
        )

    def test_binary_tree_predecessor_one_element(self):
        self.construct_tree([0])
        node = self.binary_tree.search(0)
        self.assertEqual(node.val, 0)
        self.assertEqual(
            self.binary_tree.predecessor(node), None
        )

    def test_binary_tree_predecessor_1(self):
        array = [10, 5, 15, 3, 7, 13, 18, 1, 6]
        array_sorted = sorted(array)
        self.construct_tree(array)

        for i in range(len(array_sorted)):
            cur = array_sorted[i]
            pre = array_sorted[i - 1] if i > 0 else None
            node = self.binary_tree.search(cur)
            self.assertEqual(node.val, cur)
            if pre is None:
                self.assertEqual(
                    self.binary_tree.predecessor(node), pre
                )
            else:
                self.assertEqual(
                    self.binary_tree.predecessor(node).val, pre
                )
    def test_binary_tree_search(self):
        array = [10, 5, 15, 3, 7, 13, 18, 1, 6]
        self.construct_tree(array)

        for val in array:
            self.assertEqual(self.binary_tree.search(val).val, val)

        self.assertEqual(self.binary_tree.search(-100), None)
        self.assertEqual(self.binary_tree.search(100), None)
        self.assertEqual(self.binary_tree.search(11), None)
        self.assertEqual(self.binary_tree.search(9), None)


if __name__ == "__main__":
    unittest.main()
