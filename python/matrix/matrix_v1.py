class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_rows = []
        self.matrix_cols = []

        for s in self.matrix_string.split('\n'):
            self.matrix_rows.append([int(n) for n in s.split(' ')])

        for j in range(len(self.matrix_rows[0])):
            self.matrix_cols.append([r[j] for r in self.matrix_rows])


    def row(self, index):
        return self.matrix_rows[index - 1]

    def column(self, index):
        return self.matrix_cols[index - 1]
