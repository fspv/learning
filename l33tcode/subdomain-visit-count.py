from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            cur_domain = None

            for subdomain in reversed(domain.split(".")):
                if cur_domain is None:
                    cur_domain = subdomain
                else:
                    cur_domain = subdomain + "." + cur_domain

                counter[cur_domain] += int(count)

        return [str(v) + " " + k for k, v in counter.items()]
