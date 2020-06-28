class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def is_one_edit_apart(left, right):
            edits = 0

            pos_left, pos_right = 0, 0

            while pos_left < len(left) or pos_right < len(right):
                if (
                    pos_left == len(left)
                    or pos_right == len(right)
                    or left[pos_left] != right[pos_right]
                ):
                    if edits > 0:
                        return False
                    edits += 1

                    if len(left) < len(right):
                        pos_right += 1
                    elif len(left) > len(right):
                        pos_left += 1
                    else:
                        pos_left += 1
                        pos_right += 1
                else:
                    pos_left += 1
                    pos_right += 1

            return edits == 1

        return is_one_edit_apart(s, t)
