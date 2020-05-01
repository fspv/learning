class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ptr1, ptr2 = 0, 0

        while ptr1 < len(version1) or ptr2 < len(version2):
            num1, num2 = 0, 0

            while ptr1 < len(version1) and version1[ptr1] != ".":
                num1 = num1 * 10 + int(version1[ptr1])
                ptr1 += 1
            ptr1 += 1

            while ptr2 < len(version2) and version2[ptr2] != ".":
                num2 = num2 * 10 + int(version2[ptr2])
                ptr2 += 1
            ptr2 += 1

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        return 0
