from __future__ import annotations

import string
from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True, repr=True)
class CellRange:
    top_left_row: int
    top_left_col: int
    bottom_righ_row: int
    bottom_right_col: int

    @classmethod
    def fromstring(cls, range_str: str) -> CellRange:
        if ":" in range_str:
            left, right = range_str.split(":")
        else:
            left, right = range_str, range_str

        left_row_str, left_col_str = (
            left.lstrip(string.ascii_uppercase),
            left.rstrip(string.digits),
        )

        right_row_str, right_col_str = (
            right.lstrip(string.ascii_uppercase),
            right.rstrip(string.digits),
        )

        left_row, left_col = (int(left_row_str) - 1, abs(ord("A") - ord(left_col_str)))
        right_row, right_col = (
            int(right_row_str) - 1,
            abs(ord("A") - ord(right_col_str)),
        )

        top_left_row = min(left_row, right_row)
        top_left_col = min(left_col, right_col)

        bottom_righ_row = max(left_row, right_row) + 1
        bottom_right_col = max(left_col, right_col) + 1

        return CellRange(top_left_row, top_left_col, bottom_righ_row, bottom_right_col)


class Cell(ABC):
    pass


@dataclass(repr=True)
class CellInteger(Cell):
    value: int


@dataclass(repr=True)
class CellFormulaSum(Cell):
    cell_ranges: List[CellRange] = field(default_factory=list)


@dataclass(repr=True)
class CellEmpty(Cell):
    pass


class ExcelAPI:
    def __init__(self, rows: int, cols: int) -> None:
        self._table: List[List[Cell]] = [[CellEmpty()] * cols for _ in range(rows)]
        self._cache: Dict[CellRange, int] = {}

    def set(self, row: int, col: int, value: int) -> None:
        self._table[row][col] = CellInteger(value)

    def get(self, row: int, col: int) -> int:
        cell = self._table[row][col]

        if isinstance(cell, CellEmpty):
            return 0

        if isinstance(cell, CellInteger):
            return cell.value

        if isinstance(cell, CellFormulaSum):
            self._cache = {}

            return self._resolve_sum(cell)

        raise ValueError(f"Cell type {type(cell)} is not supported")

    def _resolve_sum(self, formula_cell: CellFormulaSum) -> int:
        total = 0

        for cell_range in formula_cell.cell_ranges:
            if cell_range in self._cache:
                total += self._cache[cell_range]
                continue

            cell_range_total = 0

            for row in range(cell_range.top_left_row, cell_range.bottom_righ_row):
                for col in range(cell_range.top_left_col, cell_range.bottom_right_col):
                    cell = self._table[row][col]

                    if isinstance(cell, CellInteger):
                        cell_range_total += cell.value

                    if isinstance(cell, CellFormulaSum):
                        cell_range_total += self._resolve_sum(cell)

            self._cache[cell_range] = cell_range_total

            total += cell_range_total

        return total

    def sum(self, row: int, col: int, cell_ranges: List[CellRange]) -> int:
        cell = CellFormulaSum(cell_ranges)
        self._table[row][col] = cell

        return self.get(row, col)


class Excel:
    def __init__(self, height: int, width: str) -> None:
        self._api = ExcelAPI(height, abs(ord("A") - ord(width)) + 1)

    def set(self, row: int, column: str, val: int) -> None:
        self._api.set(row - 1, abs(ord("A") - ord(column)), val)

    def get(self, row: int, column: str) -> int:
        return self._api.get(row - 1, abs(ord("A") - ord(column)))

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        return self._api.sum(
            row - 1,
            abs(ord("A") - ord(column)),
            [CellRange.fromstring(r) for r in numbers],
        )


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
