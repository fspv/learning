from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        string_to_interval = defaultdict(lambda: [float("+inf"),0])

        def get_intervals(S):
            for pos, char in enumerate(S):
                string_to_interval[char][0] = min(
                    pos,
                    string_to_interval[char][0]
                )
                string_to_interval[char][1] = pos

        def merge_intervals(intervals):
            result = [[0, 0]]

            for new_begin, new_end in intervals:
                begin, end = result[-1]

                if new_begin <= end:
                    end = max(new_end, end)
                    result[-1] = [begin, end]
                else:
                    result.append([new_begin, new_end])

            return result

        get_intervals(S)
        intervals = merge_intervals(sorted(string_to_interval.values()))

        return [i[1] - i[0] + 1 for i in intervals]
