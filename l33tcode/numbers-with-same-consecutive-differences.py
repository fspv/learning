class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))

        result = []

        def dfs(buff, left):
            if left == 0:
                result.append(buff)
                return

            for diff in set([buff % 10 - K, buff % 10 + K]):
                if 0 <= diff < 10:
                    dfs(buff * 10 + diff, left - 1)

        for start in range(1, 10):
            dfs(start, N - 1)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.numsSameConsecDiff(3, 7) == [181,292,707,818,929]

    def test_case2(self):
        assert self.sol.numsSameConsecDiff(2, 1) == [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

    def test_case3(self):
        assert self.sol.numsSameConsecDiff(1, 0) == [0,1,2,3,4,5,6,7,8,9]

    def test_case2(self):
        assert self.sol.numsSameConsecDiff(2, 0) == [11,22,33,44,55,66,77,88,99]
