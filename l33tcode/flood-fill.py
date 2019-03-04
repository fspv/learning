class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color_to_replace = image[sr][sc]

        visited = set((sr, sc))
        stack = [(sr, sc)]
        image[sr][sc] = newColor

        while stack:
            row, column = stack.pop()

            for neigh_row, neigh_column in [
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ]:
                if 0 <= neigh_row < len(image) and \
                   0 <= neigh_column < len(image[0]) and \
                   image[neigh_row][neigh_column] == color_to_replace and \
                   not (neigh_row, neigh_column) in visited:
                    stack.append((neigh_row, neigh_column))
                    visited.add((neigh_row, neigh_column))
                    image[neigh_row][neigh_column] = newColor

        return image

    def floodFillBFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color_to_replace = image[sr][sc]

        visited = set((sr, sc))
        stack = [(sr, sc)]
        image[sr][sc] = newColor

        while stack:
            tmp_stack = stack
            stack = []

            for row, column in tmp_stack:
                for neigh_row, neigh_column in [
                    (row + 1, column),
                    (row - 1, column),
                    (row, column + 1),
                    (row, column - 1),
                ]:
                    if 0 <= neigh_row < len(image) and \
                       0 <= neigh_column < len(image[0]) and \
                       image[neigh_row][neigh_column] == color_to_replace and \
                       not (neigh_row, neigh_column) in visited:
                        stack.append((neigh_row, neigh_column))
                        visited.add((neigh_row, neigh_column))
                        image[neigh_row][neigh_column] = newColor

        return image
