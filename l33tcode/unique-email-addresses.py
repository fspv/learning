# FIXME: speed it up
# TODO: add some tests

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result_set = set()

        for email in emails:
            pos = 0
            parsed_email = ""
            while email[pos] not in ["+", "@"]:
                if email[pos] != ".":
                    parsed_email += email[pos]
                pos += 1
            while email[pos] != "@":
                pos += 1
            parsed_email += email[pos:]
            result_set.add(parsed_email)

        return len(result_set)
