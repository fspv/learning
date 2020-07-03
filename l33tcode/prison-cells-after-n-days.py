class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def process_cells_once(number: int, mask: int) -> int:
            number = ~((number << 1) ^ (number >> 1))
            number &= mask

            return number

        number = 0
        for digit in cells:
            number <<= 1
            number += digit

        mask = 0

        for _ in range(6):
            mask += 1
            mask <<= 1

        seen = {}
        count = N
        while count > 0:
            seen[number] = count
            number = process_cells_once(number, mask)
            count -= 1

            if number in seen:
                count %= seen[number] - count

        result = []

        for _ in cells:
            result.append(number % 2)

            number >>= 1

        return list(reversed(result))

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def process_cells_once(cells: List[int]) -> None:
            before, this, after = None, None, None

            for pos in range(len(cells)):
                before, this = this, cells[pos]
                after = cells[pos + 1] if pos < len(cells) - 1 else None

                if before is None or after is None:
                    cells[pos] = 0
                elif before == after:
                    cells[pos] = 1
                else:
                    cells[pos] = 0

        seen = {}
        count = N
        while count > 0:
            seen[tuple(cells)] = count
            process_cells_once(cells)
            count -= 1

            if tuple(cells) in seen:
                count %= seen[tuple(cells)] - count

        return cells
