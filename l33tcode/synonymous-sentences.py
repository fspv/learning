from typing import List
from collections import defaultdict


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        syn_map = defaultdict(set)

        for syn_pair in synonyms:
            # TODO: quite a mess. Did it during the contest, could
            # have done it much more concise
            syn_map[syn_pair[0]].add(syn_pair[1])
            syn_map[syn_pair[0]].add(syn_pair[0])
            syn_map[syn_pair[1]].add(syn_pair[0])
            syn_map[syn_pair[1]].add(syn_pair[1])
            for syn in syn_map[syn_pair[0]]:
                syn_map[syn_pair[1]].add(syn)
                syn_map[syn].add(syn_pair[1])
            for syn in syn_map[syn_pair[1]]:
                syn_map[syn_pair[0]].add(syn)
                syn_map[syn].add(syn_pair[0])

        result = []

        def construct_sentences(sentence, pos, prev):
            if pos == len(sentence):
                result.append(" ".join(prev))
                return
            if sentence[pos] in syn_map:
                for syn in list(sorted(syn_map[sentence[pos]])):
                    construct_sentences(sentence, pos + 1, prev + [syn])
            else:
                construct_sentences(sentence, pos + 1, prev + [sentence[pos]])

        construct_sentences(text.split(" "), 0, [])

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.generateSentences([["happy","joy"],["sad","sorrow"],["joy","cheerful"]], "I am happy today but was sad yesterday") == ["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
