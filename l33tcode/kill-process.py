from typing import List, Dict


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def gen_adj_list() -> Dict[int, List[int]]:
            adj_list: Dict[int, List[int]] = {}
            for pos, process in enumerate(pid):
                adj_list.setdefault(ppid[pos], [])
                adj_list[ppid[pos]].append(process)

            return adj_list

        adj_list = gen_adj_list()

        result: List[int] = []

        stack: List[int] = [kill]

        while stack:
            process = stack.pop()
            result.append(process)

            for child_process in adj_list.get(process, []):
                stack.append(child_process)

        return result
