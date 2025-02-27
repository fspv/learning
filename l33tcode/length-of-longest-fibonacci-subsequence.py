class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        num_to_prev_length: dict[int, dict[int, int]] = { n: {} for n in arr}

        arr.sort()

        longest = 0

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] - arr[j] in num_to_prev_length[arr[j]]:
                    length = num_to_prev_length[arr[j]][arr[i] - arr[j]] + 1
                    num_to_prev_length[arr[i]][arr[j]] = length
                    longest = max(longest, length)
                else:
                    num_to_prev_length[arr[i]][arr[j]] = 2

        return longest
