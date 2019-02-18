# FIXME: speed it up
# TODO: add some tests

class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        filtered_emails = set()

        for email in emails:
            remove = False
            at_reached = False
            email_filtered_list = []

            for symbol in email:
                if not at_reached and symbol == ".":
                    continue
                elif symbol == "+":
                    remove = True
                elif symbol == "@":
                    remove = False
                    at_reached = True
                else:
                    if not remove:
                        email_filtered_list.append(symbol)

            filtered_emails.add("".join(email_filtered_list))

        return len(filtered_emails)
