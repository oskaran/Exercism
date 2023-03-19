from typing import List

class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix_rows = [[int(n) for n in s.split()] for s in matrix_string.splitlines()]

    def row(self, index: int) -> List[int]:
        return self.matrix_rows[index - 1]

    def column(self, index: int) -> List[int]:
        return [r[index - 1] for r in self.matrix_rows]
