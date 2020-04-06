import string
from collections import defaultdict, Counter
from typing import List


class Solution:
    def groupAnagramsCountMap(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for word in strs:
            counter = Counter()

            for letter in word:
                counter[string.ascii_lowercase.index(letter)] += 1

            key = frozenset(counter.items())
            str_map[key].append(word)

        return list(str_map.values())

    def groupAnagramsAlphabetMap(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for word in strs:
            str_hash = [0] * 26
            for letter in word:
                str_hash[string.ascii_lowercase.index(letter)] += 1

            str_map[tuple(str_hash)].append(word)

        return list(str_map.values())

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




class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"],
        ]
