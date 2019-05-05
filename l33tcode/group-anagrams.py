class Solution:
    def groupAnagrams(self, strs):
        dict_with_rep = {}
        dict_without_rep = {}

        for word in strs:
            tmp_set = set()
            rep = False
            for char in word:
                if char not in tmp_set:
                    tmp_set.add(char)
                else:
                    rep = True
                    break

            if rep:
                s_word = "".join(sorted(word))
                if s_word not in dict_with_rep:
                    dict_with_rep[s_word] = []
                dict_with_rep[s_word].append(word)
            else:
                s_word = frozenset(tmp_set)
                if s_word not in dict_with_rep:
                    dict_with_rep[s_word] = []
                dict_with_rep[s_word].append(word)

        result = []

        for arr in list(dict_with_rep.values()) + list(dict_without_rep.values()):
            result.append(arr)

        return result
