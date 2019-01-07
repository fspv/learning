from stack import ArrayStack

class BinaryTreeNode():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = None

    def _search(self, key, root):
        node = root

        if key < node.key:
            if node.left is not None:
                return self._search(key, node.left)
        elif key > node.key:
            if node.right is not None:
                return self._search(key, node.right)
        elif key == node.key:
            return node

    def _search_parent(self, key, root):
        node = root

        if key < node.key:
            if node.left is not None:
                return self._search_parent(key, node.left)
            else:
                return node
        elif key > node.key:
            if node.right is not None:
                return self._search_parent(key, node.right)
            else:
                return node
        elif key == node.key:
            return root

    def search(self, key):
        return self._search(key, self.root)

    def insert(self, key):
        new_node = BinaryTreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            node = self._search_parent(key, self.root)
            if key < node.key:
                node.left = new_node
            elif key > node.key:
                node.right = new_node

    def __str__(self, root=None):
        if root is None:
            root = self.root

        left_keys = self.__str__(root.left) if root.left is not None else []
        right_keys = self.__str__(root.right) if root.right is not None else []

        keys = [root.key] +  left_keys + right_keys

        if root == self.root:
            return str(keys)
        else:
            return keys

    def print_non_recursive(self):
        node = root
        tmp_stack = ArrayStack(666)
        tmp_stack.push(node)

        while not tmp_stack.stack_empty():
            tmp_stack.push(node)
            node = node.left


# Tests
tree = BinaryTree()
tree.insert(20)
tree.insert(10)
tree.insert(15)
tree.insert(5)
tree.insert(39)
tree.insert(31)
tree.insert(50)
tree.insert(5)
tree.insert(2)
tree.insert(20)
tree.insert(100)

print(tree)
