from typing import List, Dict

def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    if len({len(row) for row in matrix}) > 1:
        raise ValueError("Irregular Matrix")

    # Possible saddle points coordinates in each row
    t_rows = {(i, j) for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)}
    # select only the columns with possible saddle points
    sel_cols = {t[1] for t in t_rows}
    columns = [[r[c] for r in matrix] for c in sel_cols]
    t_cols = {(i, j) for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)}

    return [{'row': (t[0] + 1), 'column': (t[1] + 1)} for t in list(t_rows.intersection(t_cols))]

#squeakyboots
def saddle_points_squeakyboots(matrix):
    try:
        return [dict(row=r + 1, column=c + 1) for c, r in
                [(i, j) for i in range(len(matrix[0])) for j in range(len(matrix))]  # each possible coordinate
                if max(matrix[r]) <= matrix[r][c] <= min([r[c] for r in matrix])]
    except IndexError:
        if not matrix:
            return matrix
        raise ValueError("The input matrix is irregular.")

#DrizzlingVoid
def saddle_points_drizzling(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("matrix shape not valid")

    t_mat = list(zip(*matrix))
    return [{"row": m+1, "column":n+1}  for m, row in enumerate(matrix)
                                        for n, val in enumerate(row)
                                        if val == max(row) and val == min(t_mat[n])]

