class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for substring_length in range(1, len(s) // 2 + 1):
            if len(s) % substring_length != 0:
                continue

            first_part = s[0:substring_length]

            for part in range(len(s) // substring_length):
                start = substring_length * part
                end = substring_length * (part + 1)
                if first_part != s[start:end]:
                    break
            else:
                return True

        return False
