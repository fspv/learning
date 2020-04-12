from typing import List
from itertools import islice
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        emails_set = set()

        for account in accounts:
            for email in islice(account, 1, len(account)):
                email_to_name[email] = account[0]
                emails_set.add(email)

        email_to_pos = {k: v for v, k in enumerate(emails_set)}
        pos_to_email = {k: v for k, v in enumerate(emails_set)}
        emails = list(range(len(emails_set)))
        count = [1] * len(emails)

        def find_root(array, pos):
            root = pos

            while array[root] != root:
                root = array[root]

            while pos != root:
                array[pos], pos = root, array[pos]

            return root

        for account in accounts:
            for pos in range(2, len(account)):
                cur, prev = account[pos - 1], account[pos]
                cur_pos, prev_pos = email_to_pos[cur], email_to_pos[prev]

                root_cur = find_root(emails, cur_pos)
                root_prev = find_root(emails, prev_pos)

                if root_cur != root_prev:
                    if count[root_cur] > count[root_prev]:
                        emails[root_cur] = emails[root_prev]
                        count[root_cur] += count[root_prev]
                    else:
                        emails[root_prev] = emails[root_cur]
                        count[root_prev] += count[root_cur]

        tmp = defaultdict(list)

        for pos in range(len(emails)):
            root = find_root(emails, pos)
            tmp[root].append(pos_to_email[pos])

        return [[email_to_name[pos_to_email[k]]] + sorted(v) for k, v in tmp.items()]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert sorted(
            self.sol.accountsMerge(
                [
                    ["John", "johnsmith@mail.com", "john00@mail.com"],
                    ["John", "johnnybravo@mail.com"],
                    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                    ["Mary", "mary@mail.com"],
                ]
            )
        ) == sorted(
            [
                ["Mary", "mary@mail.com"],
                [
                    "John",
                    "john00@mail.com",
                    "john_newyork@mail.com",
                    "johnsmith@mail.com",
                ],
                ["John", "johnnybravo@mail.com"],
            ]
        )
