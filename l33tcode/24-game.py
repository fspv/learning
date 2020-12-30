from itertools import combinations, permutations
from typing import List, Union, Optional, Tuple, Set


class TreeNode:
    def __init__(self, operation: bool, value: Optional[int] = None) -> None:
        self.value = value
        self.operation = operation
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f"TreeNode({self.operation}, {self.value})"


def perform_operation(operation: str, left: float, right: float) -> float:
    if operation == "*":
        return left * right
    elif operation == "-":
        return left - right
    elif operation == "+":
        return left + right
    elif operation == "/":
        return left / right

    raise NotImplementedError()


def build_trees() -> List[TreeNode]:
    trees: List[TreeNode] = []

    node0, node1, node2, node3 = (
        TreeNode(False, 0),
        TreeNode(False, 1),
        TreeNode(False, 2),
        TreeNode(False, 3),
    )

    node4, node5, node6 = TreeNode(True), TreeNode(True), TreeNode(True)

    node4.left, node4.right = node0, node1
    node5.left, node5.right = node4, node2
    node6.left, node6.right = node5, node3

    trees.append(node6)

    node0, node1, node2, node3 = (
        TreeNode(False, 0),
        TreeNode(False, 1),
        TreeNode(False, 2),
        TreeNode(False, 3),
    )

    node4, node5, node6 = TreeNode(True), TreeNode(True), TreeNode(True)

    node4.left, node4.right = node0, node1
    node5.left, node5.right = node2, node3
    node6.left, node6.right = node4, node5

    trees.append(node6)

    node0, node1, node2, node3 = (
        TreeNode(False, 0),
        TreeNode(False, 1),
        TreeNode(False, 2),
        TreeNode(False, 3),
    )

    node4, node5, node6 = TreeNode(True), TreeNode(True), TreeNode(True)

    node4.left, node4.right = node2, node3
    node5.left, node5.right = node1, node4
    node6.left, node6.right = node0, node5

    trees.append(node6)

    return trees


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def dfs(
            tree_node: TreeNode, operations: List[str], numbers: Tuple[int, ...]
        ) -> float:
            if tree_node.operation:
                operation = operations.pop()
                node_left, node_right = tree_node.left, tree_node.right
                if node_left and node_right:
                    return perform_operation(
                        operation,
                        dfs(node_left, operations, numbers),
                        dfs(node_right, operations, numbers),
                    )
            elif tree_node.value is not None:
                return float(numbers[tree_node.value])

            raise ValueError("Tree node should either be an operation or have a value")

        operations_choices: List[str] = []
        operations_choices.extend(["*"] * 3)
        operations_choices.extend(["+"] * 3)
        operations_choices.extend(["-"] * 3)
        operations_choices.extend(["/"] * 3)

        operations_distinct: Set[Tuple[str, ...]] = set()
        for operations_sorted in combinations(operations_choices, 3):
            for operations in permutations(operations_sorted):
                operations_distinct.add(operations)

        trees: List[TreeNode] = build_trees()

        for numbers in permutations(nums):
            for tree_root in trees:
                for operations in operations_distinct:
                    try:
                        result = dfs(tree_root, list(reversed(operations)), numbers)
                        if abs(result - 24) < 0.001:
                            return True
                    except ZeroDivisionError:
                        pass

        return False
