from functools import lru_cache


class Solution:
    def countSubstrings(self, string1: str, string2: str) -> int:
        count = 0
        for pos1 in range(len(string1)):
            for pos2 in range(len(string2)):
                replaced = False
                cur_pos1, cur_pos2 = pos1, pos2
                while (
                    cur_pos1 < len(string1)
                    and cur_pos2 < len(string2)
                    and (string1[cur_pos1] == string2[cur_pos2] or not replaced)
                ):
                    if string1[cur_pos1] != string2[cur_pos2]:
                        replaced = True
                    count += int(replaced)
                    cur_pos1 += 1
                    cur_pos2 += 1

        return count
