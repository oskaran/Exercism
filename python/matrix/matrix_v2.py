"""
List comprehensions are the Pythonic approach to generating a list from an iterable.
Can you find and replace this pattern in your code?

out = []
for a in b:
    out.append(func(a))
# vs
out = [func(a) for a in b]

"""

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_rows = []

        for s in matrix_string.splitlines():
            self.matrix_rows.append([int(n) for n in s.split()])

    def row(self, index):
        return self.matrix_rows[index - 1]

    def column(self, index):
        return [r[index - 1] for r in self.matrix_rows]
