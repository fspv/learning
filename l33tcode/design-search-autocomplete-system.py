import heapq
from collections import defaultdict


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.rev_idx = defaultdict(lambda: list())
        self.sentence_buffer = ""

        for sentence, times in zip(sentences, times):
            self._add_sentence(sentence, times)

    def _add_sentence(self, sentence, times):
        for pos in range(len(sentence)):
            for sub_pos in range(len(self.rev_idx[sentence[:pos + 1]])):
                c, s = self.rev_idx[sentence[:pos + 1]][sub_pos]
                if s == sentence:
                    self.rev_idx[sentence[:pos + 1]][sub_pos] = (c + times, sentence)
                    break
            else:
                self.rev_idx[sentence[:pos + 1]].append((times, sentence))

            #heapq.heapify(self.rev_idx[sentence[:pos + 1]])

            self.rev_idx[sentence[:pos + 1]].sort(key=lambda x: str(10000 - x[0]) + x[1])

    def _get_top_k_for_substr(self, substr, k):
        #tmp = []
        #prev_times = 0
        #result = []

        #for times, sentence in heapq.nlargest(k, self.rev_idx[substr], lambda x: x[0]):
        #    if times != prev_times:
        #        result.extend(sorted(tmp))
        #        tmp = []

        #    prev_times = times

        #    tmp.append(sentence)

        #result.extend(sorted(tmp))

        return [s for c, s in self.rev_idx[substr][:k]]

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.sentence_buffer += c
        else:
            self._add_sentence(self.sentence_buffer, 1)
            self.sentence_buffer = ""

        return self._get_top_k_for_substr(self.sentence_buffer, 3)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
