import abc
from enum import Enum
from typing import Optional, List, Callable

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Operation(Enum):
    ADD = "+"
    SUBSTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


def action_factory(operation: Operation) -> Callable:
    if operation == Operation.ADD:
        return lambda x, y: x + y
    elif operation == Operation.SUBSTRACT:
        return lambda x, y: x - y
    elif operation == Operation.MULTIPLY:
        return lambda x, y: x * y
    elif operation == Operation.DIVIDE:
        return lambda x, y: x / y

    return lambda x, y: NotImplementedError()


class Node(abc.ABC):
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    @abc.abstractmethod
    def evaluate(self) -> int:
        pass


class OperationNode(Node):
    def __init__(self, operation: Operation) -> None:
        self._operation = operation

    def __repr__(self) -> str:
        return f"OperationNode({self._operation}), left={self.left}, right={self.right}"

    def evaluate(self) -> float:
        action = action_factory(self._operation)

        node_left, node_right = self.left, self.right

        if not node_left or not node_right:
            raise ValueError()

        return int(action(node_left.evaluate(), node_right.evaluate()))


class ValueNode(Node):
    def __init__(self, value: int) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"ValueNode({self._value}), left={self.left}, right={self.right}"

    def evaluate(self) -> int:
        return self._value


"""
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> Optional[Node]:
        stack: List[Node] = []

        operations = {
            Operation.ADD.value,
            Operation.SUBSTRACT.value,
            Operation.MULTIPLY.value,
            Operation.DIVIDE.value,
        }

        for item in postfix:
            operation = item in operations
            node = OperationNode(Operation(item)) if operation else ValueNode(int(item))
            if len(stack) > 1 and operation:
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
            else:
                stack.append(node)

        if not stack:
            return None

        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
