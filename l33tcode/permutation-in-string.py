class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        for s in s1:
            if s in s1_dict:
                s1_dict[s] += 1
            else:
                s1_dict[s] = 1

        s2_sub_dict = {}
        for s in s2[:len(s1)]:
            if s in s2_sub_dict:
                s2_sub_dict[s] += 1
            else:
                s2_sub_dict[s] = 1

        if s1_dict == s2_sub_dict:
            return True

        for pos in range(1, len(s2) - len(s1) + 1):
            s2_sub_dict[s2[pos - 1]] -= 1
            if s2_sub_dict[s2[pos - 1]] == 0:
                s2_sub_dict.pop(s2[pos - 1])
            if s2[pos + len(s1) - 1] in s2_sub_dict:
                s2_sub_dict[s2[pos + len(s1) - 1]] += 1
            else:
                s2_sub_dict[s2[pos + len(s1) - 1]] = 1

            if s1_dict == s2_sub_dict:
                return True

        return False

    def checkInclusionBF(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        for s in s1:
            if s in s1_dict:
                s1_dict[s] += 1
            else:
                s1_dict[s] = 1

        for pos in range(len(s2) - len(s1) + 1):
            s1_dict_local = s1_dict.copy()
            for sub_pos in range(pos, pos + len(s1)):
                if s2[sub_pos] in s1_dict_local and \
                   s1_dict_local[s2[sub_pos]] > 0:
                    s1_dict_local[s2[sub_pos]] -= 1
                    if s1_dict_local[s2[sub_pos]] == 0:
                        s1_dict_local.pop(s2[sub_pos])
                else:
                    break

            if len(s1_dict_local) == 0:
                return True

        return False
