from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dp(ptr1: int, ptr2: int, ptr3: int) -> bool:
            if ptr3 == len(s3):
                return ptr1 == len(s1) and ptr2 == len(s2)

            result = False

            if ptr1 < len(s1) and s1[ptr1] == s3[ptr3]:
                result = result or dp(ptr1 + 1, ptr2, ptr3 + 1)

            if ptr2 < len(s2) and s2[ptr2] == s3[ptr3]:
                result = result or dp(ptr1, ptr2 + 1, ptr3 + 1)

            return result

        return dp(0, 0, 0)
