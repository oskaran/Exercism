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

matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
#cols = len(matrix[0])
#for row in matrix:
#    loc_row = [i for i, v in enumerate(row) if v == max(row)]
# Possible indexes of saddle points in each row List[List]
loc_rows = [[i for i, v in enumerate(row) if v == max(row)] for row in matrix]
c_rows = [(i, j) for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)]
#[{'row': i, 'column': j} for i, row in enumerate(matrix) for j, v in enumerate(row) if v == max(row)]

#cols = [val for rows in loc_rows for val in rows]
# select only the columns with a possible saddle point
sel_cols = {t[1] for t in c_rows}
columns = [[r[c] for r in matrix] for c in sel_cols]

#vamos = [[j for j, v in enumerate(col) if v == min(col)] for col in [[r[index] for r in matrix] for index in cols]]
c_cols = [(i, j) for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)]
#[{'row': i, 'column': j} for j, col in zip(sel_cols, columns) for i, v in enumerate(col) if v == min(col)]


for srow in loc_rows:
    [[r[index] for r in matrix] for index in srow]

#cols = [[r[j] for r in matrix] for j in range(len(matrix[0]))]
    [r[c] for c in loc_row for r in matrix]






[r[index] for r in matrix]

