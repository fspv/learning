import operator
from typing import List, Set


class Solution:
    def addOperators(self, nums: str, target: int) -> List[str]:
        stack: List[str] = []
        result: Set[str] = set()

        def backtrack(pos: int, total: int, last: int) -> None:
            if pos == len(nums):
                if total == target:
                    result.add("".join(stack))

                return

            for size in range(1, len(nums) - pos + 1):
                if nums[pos] == "0" and size > 1:
                    break

                num = int(nums[pos : pos + size])

                for op, _repr, last_result in [
                    (operator.add, "+", 0),
                    (operator.sub, "-", 0),
                    (operator.mul, "*", last),
                ]:
                    diff = op(last_result, num)
                    stack.append(_repr)
                    stack.append(str(num))
                    backtrack(pos + size, total - last_result + diff, diff)
                    stack.pop()
                    stack.pop()

        for size in range(1, len(nums) + 1):
            if nums[0] == "0" and size > 1:
                break

            num = int(nums[0:size])
            stack.append(str(num))
            backtrack(size, num, num)
            stack.pop()

        return list(result)
