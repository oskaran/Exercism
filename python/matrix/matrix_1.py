class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string


    def row(self, index):
        pass

    def column(self, index):
        pass


def matrix(matrix_string):

    mr = []
    for s in matrix_string.split('\n'):
        mr.append([int(n) for n in s.split(' ')])

    mc = []
    for j in range(len(mr[0])):
        mc.append([r[j] for r in mr])

    return (mr[:], mc[:])


def matrix1(matrix_string):

    mr = []
    for s in matrix_string.split('\n'):
        mr.append([int(n) for n in s.split(' ')])

    #ren = len(mr), col = len(mr[0])
    mc = [[0 for i in range(len(mr))] for j in range(len(mr[0]))]
    for i in range(len(mr)):
        for j in range(len(mr[0])):
            mc[j][i] = mr[i][j]

    mc = []
    for j in range(len(mr[0])):
        mc.append([r[j] for r in mr])

    """
    matrix_slist = matrix_string.split('\n')
    m0 = []
    for s in matrix_slist:
        #mr.append(s.split(' '))
        for n in s.split(' '):
            m0.append(n)
     [m0.append(n) for s in matrix_slist for n in s.split(' ')]
    """
    return mr[:]