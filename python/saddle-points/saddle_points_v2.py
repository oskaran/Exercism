"""
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2     <--- saddle point at column 1, row 2, with value 5
3 | 6  6  7

It has a saddle point at column 1, row 2.
It's called a "saddle point" because it is greater than or equal to every element
in its row and less than or equal to every element in its column.

A matrix may have zero or more saddle points.

Your code should be able to provide the (possibly empty) list of all the saddle points
for any given matrix.
"""
#[{"row": 2, "column": 1}]
    #row: >= than elements
    #col: <= than elements
def saddle_points_d(matrix):
    # Possible coordinates of saddle points in each row
    #t_rows = [(i, j) for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)]
    c_rows = [{'row': i, 'column': j} for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)]

    # select only the columns with possible saddle points
    #sel_cols = {t[1] for t in t_rows}
    sel_cols = {d['column'] for d in c_rows}
    columns = [[r[c] for r in matrix] for c in sel_cols]

    #t_cols = [(i, j) for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)]
    c_cols = [{'row': i, 'column': j} for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)]

    inter = [d for d in c_rows if d in c_cols]
#    ble = list(set(t_rows) & set(t_cols))

    return [{'row': (d['row'] + 1), 'column': (d['column'] + 1)} for d in inter]

def saddle_points(matrix):
    # Possible coordinates of saddle points in each row
    t_rows = {(i, j) for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)}
    #c_rows = [{'row': i, 'column': j} for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)]

    # select only the columns with possible saddle points
    sel_cols = {t[1] for t in t_rows}
    #sel_cols = {d['column'] for d in c_rows}
    columns = [[r[c] for r in matrix] for c in sel_cols]

    t_cols = {(i, j) for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)}
    #c_cols = [{'row': i, 'column': j} for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)]

    #inter = [d for d in c_rows if d in c_cols]
    #inter = list(t_rows.intersection(t_cols))

    return [{'row': (t[0] + 1), 'column': (t[1] + 1)} for t in list(t_rows.intersection(t_cols))]

#matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
[{"row": 1, "column": 2}, {"row": 2, "column": 2}, {"row": 3, "column": 2}]
"""
test_can_identify_multiple_saddle_points_in_a_column

    1  2  3
  |---------
1 | 4  5  4
2 | 3  5  5     <--- saddle point at column x, row x, with value x
3 | 1  5  4

"""