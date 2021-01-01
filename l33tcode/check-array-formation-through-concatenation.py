from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        first_piece_map = {pieces[pos][0]: pos for pos in range(len(pieces))}

        pos = 0

        while pos < len(arr):
            if not arr[pos] in first_piece_map:
                return False

            cur_pieces = pieces[first_piece_map[arr[pos]]]

            if cur_pieces == arr[pos : pos + len(cur_pieces)]:
                pos += len(cur_pieces)
            else:
                return False

        return True
