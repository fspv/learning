class Solution:
    def validPalindrome(self, s: str) -> bool:
        def search(left: int, right: int, deleted: int) -> bool:
            if left >= right:
                return True
            elif s[left] == s[right]:
                return search(left + 1, right - 1, deleted)
            elif deleted == 0:
                return search(left + 1, right, deleted + 1) or search(left, right - 1, deleted + 1)
            else:
                return False

        return search(0, len(s) - 1, 0)
