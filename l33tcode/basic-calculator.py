import string
from enum import Enum
from typing import List, Optional, Tuple, Union


class Operation(Enum):
    ADD = 0
    SUBSTRACT = 1


class ExpressionTreeNodeType(Enum):
    OPERATION = 0
    CONSTANT = 0


class ExpressionTreeNode:
    def __init__(
        self,
        node_type: ExpressionTreeNodeType,
        value: Optional[int],
        operation: Optional[Operation],
    ) -> None:
        self.node_type = node_type
        self.value = value
        self.operation = operation
        self.left: Optional[ExpressionTreeNode] = None
        self.right: Optional[ExpressionTreeNode] = None


class Solution1:
    def calculate(self, expression: str) -> int:
        def get_number(pos: int) -> Tuple[int, int]:
            number = 0
            offset = 0

            while expression[pos] in string.digits:
                number *= 10
                number += int(expression[pos])
                offset += 1
                pos += 1

            return offset, number

        def calculate(sub_expression: List[Union[int, str]]) -> int:
            result = 0
            sign = 1

            for val in sub_expression:
                if isinstance(val, int):
                    result += sign * val
                elif val == "+":
                    sign = 1
                elif val == "-":
                    sign = -1

            return result

        expression = "(" + expression + ")"

        stack: List[Union[int, str]] = []

        pos = 0

        while pos < len(expression):
            if expression[pos] == " ":
                pos += 1
            elif expression[pos] == "(":
                pos += 1
                stack.append("(")
            elif expression[pos] == ")":
                pos += 1
                tmp: List[Union[int, str]] = []
                while stack[-1] != "(":
                    tmp.append(stack.pop())

                tmp.reverse()

                number = calculate(tmp)

                stack.pop()
                stack.append(number)

            elif expression[pos] == "+":
                pos += 1
                stack.append("+")
            elif expression[pos] == "-":
                pos += 1
                stack.append("-")
            else:
                offset, number = get_number(pos)

                stack.append(number)
                pos += offset

        return int(stack[-1])


class Calculator:
    def __init__(self) -> None:
        pass

    def _get_integer(self, pos: int, expression: str) -> Tuple[int, int]:
        result = 0

        while pos < len(expression) and expression[pos].isdigit():
            result *= 10
            result += int(expression[pos])
            pos += 1

        return pos, result

    def _get_subtree(self, pos: int, expression: str) -> Tuple[int, ExpressionTreeNode]:
        if expression[pos] == "(":
            return self._parse(pos + 1, expression)
        else:
            pos, constant = self._get_integer(pos, expression)
            return (
                pos,
                ExpressionTreeNode(ExpressionTreeNodeType.CONSTANT, constant, None),
            )

    def _parse(self, pos: int, expression: str) -> Tuple[int, ExpressionTreeNode]:
        pos, left = self._get_subtree(pos, expression)

        while expression[pos] in "+-":
            operation = Operation.ADD if expression[pos] == "+" else Operation.SUBSTRACT
            pos, right = self._get_subtree(pos + 1, expression)
            node = ExpressionTreeNode(ExpressionTreeNodeType.OPERATION, None, operation)
            node.left = left
            node.right = right

            left = node

        pos += 1

        return pos, left

    def _calculate(self, node: ExpressionTreeNode) -> int:
        if (
            node.node_type == ExpressionTreeNodeType.OPERATION
            and node.left
            and node.right
        ):
            if node.operation == Operation.ADD:
                return self._calculate(node.left) + self._calculate(node.right)
            else:
                return self._calculate(node.left) - self._calculate(node.right)
        else:
            if node.value is None:
                raise ValueError("Constant node value cannot be None")
            return node.value

    def calculate(self, expression: str) -> int:
        expression = "(" + expression.replace(" ", "") + ")"

        _, node = self._get_subtree(0, expression)

        return self._calculate(node)

    def _parse_expression(self, expression: str) -> List[Union[str, int]]:
        pos = 0
        result: List[Union[str, int]] = []

        while pos < len(expression):
            if expression[pos] in "-+()":
                result.append(expression[pos])
                pos += 1
            elif expression[pos][0].isdigit():
                pos, number = self._get_integer(pos, expression)
                result.append(number)
            else:
                pos += 1

        return result

    def calculate2(self, expression: str) -> int:
        parsed_expression = self._parse_expression(expression)
        prefix_stack: List[Union[str, int]] = []
        operator_stack: List[Union[str, int]] = []

        pos = 0

        for pos in range(len(parsed_expression)):
            if isinstance(parsed_expression[pos], int):
                prefix_stack.append(int(parsed_expression[pos]))
            elif str(parsed_expression[pos]) in "+-":
                while operator_stack and operator_stack[-1] == "-":
                    prefix_stack.append(operator_stack.pop())

                operator_stack.append(parsed_expression[pos])
            elif parsed_expression[pos] == "(":
                operator_stack.append(parsed_expression[pos])
            elif parsed_expression[pos] == ")":
                while operator_stack and operator_stack[-1] != "(":
                    prefix_stack.append(operator_stack.pop())
                operator_stack.pop()
            else:
                raise NotImplementedError("Type of input is not supported")

        while operator_stack:
            prefix_stack.append(operator_stack.pop())

        stack: List[Union[str, int]] = []

        for value in reversed(prefix_stack):
            stack.append(value)
            while len(stack) > 2:
                operation, right, left = stack[-3:]
                if (
                    str(operation) in "-+"
                    and isinstance(left, int)
                    and isinstance(right, int)
                ):
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    if operation == "+":
                        stack.append(left + right)
                    else:
                        stack.append(left - right)
                else:
                    break

        return int(stack.pop())


class Solution:
    def calculate(self, s: str) -> int:
        calculator = Calculator()
        return calculator.calculate2(s)
