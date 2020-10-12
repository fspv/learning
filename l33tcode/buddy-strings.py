class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        first, second = -1, -1
        replacements = 0
        pos = 0

        while pos < len(A):
            if A[pos] != B[pos]:
                replacements += 1

                if replacements > 2:
                    return False

                first, second = second, pos

            pos += 1

        if replacements > 2:
            return False
        elif replacements == 2:
            if (A[first], A[second]) != (B[second], B[first]):
                return False
        elif replacements == 1:
            return False
        else:
            return len(set(A)) != len(A)

        return True
