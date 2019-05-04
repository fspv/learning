class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        visited = [[False for _ in matrix[0]] for _ in matrix]
        result = []

        row, col = 0, 0
        vec = (0, 1)

        while row != len(matrix) and not visited[row][col]:
            visited[row][col] = True

            result.append(matrix[row][col])

            row, col = tuple(map(lambda x, y: x + y, (row, col), vec))

            if row == len(matrix) or col == len(matrix[0]) or visited[row][col]:
                row, col = tuple(map(lambda x, y: x - y, (row, col), vec))
                vec = (vec[1], - vec[0])
                row, col = tuple(map(lambda x, y: x + y, (row, col), vec))

        return result
