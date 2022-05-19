from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpet_len: int) -> int:
        tiles.sort()

        # Right side of the carpet
        right = 0

        # Tiles covered by cover completely
        tiles_covered = 0

        result = 0

        for left in range(len(tiles)):
            # Predicate: carpet should cover all the tiles completely all the time
            # Right pointer after the loop might point to a tile that isn't
            # covered by the carpet at all, or partially covered
            while right < len(tiles) and tiles[right][1] < tiles[left][0] + carpet_len:
                tiles_covered += tiles[right][1] - tiles[right][0] + 1
                right += 1

            # Add a tile that might be covered partially
            additional = max(
                0,
                tiles[left][0] + carpet_len - tiles[right][0]
                if right < len(tiles)
                else 0,
            )

            result = max(result, tiles_covered + additional)

            # Handle situation when right pointer didn't move
            if left < right:
                tiles_covered -= tiles[left][1] - tiles[left][0] + 1
            else:
                right = left + 1

        return result
