from enum import Enum
from typing import List, Iterator, Tuple


class GridCharacter(Enum):
    SPACE = 0
    SLASH = 1
    BACKSLASH = 2


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def neighbours(
            visited: List[List[bool]], row: int, col: int, rows: int, cols: int
        ) -> Iterator[Tuple[int, int]]:
            for neigh_row, neigh_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if (
                    0 <= neigh_row < rows
                    and 0 <= neigh_col < cols
                    and not visited[neigh_row][neigh_col]
                ):
                    yield neigh_row, neigh_col

        def paint(
            visited: List[List[bool]], row: int, col: int, rows: int, cols: int
        ) -> None:
            visited[row][col] = True

            for neigh_row, neigh_col in neighbours(visited, row, col, rows, cols):
                paint(visited, neigh_row, neigh_col, rows, cols)

        def grid_normalize(grid: List[str]) -> List[List[GridCharacter]]:
            grid_normalized: List[List[GridCharacter]] = [[] for _ in grid]

            for row in range(len(grid)):
                pos = 0

                while pos < len(grid[row]):
                    if grid[row][pos] == " ":
                        grid_normalized[row].append(GridCharacter.SPACE)
                        pos += 1
                    elif grid[row][pos] == "/":
                        grid_normalized[row].append(GridCharacter.SLASH)
                        pos += 1
                    else:
                        grid_normalized[row].append(GridCharacter.BACKSLASH)
                        pos += 1

            return grid_normalized

        def grid_to_picture(grid: List[str]) -> List[List[bool]]:
            grid_normalized = grid_normalize(grid)

            grid_rows, grid_cols = (
                len(grid_normalized),
                len(grid_normalized[0]) if grid_normalized else 0,
            )

            picture_rows, picture_cols = grid_rows * 3 + 1, grid_cols * 3 + 1

            picture = [[False] * picture_cols for _ in range(picture_rows)]

            for grid_row in range(grid_rows):
                for grid_col in range(grid_cols):
                    if grid_normalized[grid_row][grid_col] == GridCharacter.BACKSLASH:
                        top_left_row, top_left_col = grid_row * 3, grid_col * 3

                        for offset in range(4):
                            picture[top_left_row + offset][top_left_col + offset] = True
                    elif grid_normalized[grid_row][grid_col] == GridCharacter.SLASH:
                        top_right_row, top_right_col = grid_row * 3, grid_col * 3 + 3

                        for offset in range(4):
                            picture[top_right_row + offset][
                                top_right_col - offset
                            ] = True

            return picture

        picture: List[List[bool]] = grid_to_picture(grid)

        rows, cols = len(picture), len(picture[0]) if picture else 0

        regions = 0
        for row in range(rows):
            for col in range(cols):
                if not picture[row][col]:
                    paint(picture, row, col, rows, cols)
                    regions += 1

        return regions
