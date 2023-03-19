from typing import List, Dict

def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    if len({len(row) for row in matrix}) > 1:
        raise ValueError("Irregular Matrix")

    return [{'row':r + 1, 'column':c + 1} for r, c in [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
            if max(matrix[r]) <= matrix[r][c] <= min([row[c] for row in matrix])]