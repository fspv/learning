from typing import List, DefaultDict, Set
from collections import defaultdict


class Solution:
    def grayCode(self, n: int) -> List[int]:
        def gen_adj_list(bits: int) -> DefaultDict[int, List[int]]:
            adj_list: DefaultDict[int, List[int]] = defaultdict(list)

            stack: List[int] = [0]
            seen: Set[int] = {0}

            while stack:
                num = stack.pop()

                for bit in range(bits):
                    new_num = num ^ (1 << bit)

                    adj_list[num].append(new_num)

                    if new_num not in seen:
                        stack.append(new_num)
                        seen.add(new_num)

            return adj_list

        adj_list = gen_adj_list(n)

        seen: Set[int] = set()

        stack: List[int] = [0]

        result: List[int] = [0]

        while stack:
            num = stack.pop()
            seen.add(num)

            for adj_num in adj_list[num]:
                if adj_num not in seen:
                    stack.append(adj_num)
                    result.append(adj_num)
                    break

        return result
