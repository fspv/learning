class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        pos = len(S) - 1
        actual_pos = 0

        alphanum = set(x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "0123456789")
        output = []

        while pos >= 0:
            if S[pos] in alphanum:
                if actual_pos > 0 and actual_pos % K == 0:
                    output += ["-"]
                output += [S[pos].upper()]
                actual_pos += 1

            pos -= 1

        return "".join(reversed(output))
