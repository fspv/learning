class Solution:
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = [1] * N
        adj = [set() for _ in range(N)]

        for edge in paths:
            begin, end = edge[0] - 1, edge[1] - 1
            adj[begin].add(end)
            adj[end].add(begin)
            if result[end] == result[begin]:
                avail = set([1, 2, 3, 4])
                for garden in adj[end]:
                    avail.discard(result[garden])
                result[end] = avail.pop()

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.gardenNoAdj(0, []) == []

    def test_custom1(self):
        assert self.sol.gardenNoAdj(3, [[1,2],[2,3],[3,1]]) == [3, 2, 1]

    def test_custom2(self):
        assert self.sol.gardenNoAdj(4, [[1,2],[3,4]]) == [1, 2, 1, 2]

    def test_custom3(self):
        assert self.sol.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]) == [1, 2, 3, 4]

    def test_custom4(self):
        assert self.sol.gardenNoAdj(5, [[1,2],[3,4],[4,1],[1,3],[2,4],[5,2]]) == [1, 2, 3, 4, 1]
