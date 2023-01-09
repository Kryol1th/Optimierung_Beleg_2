import numpy as np

c = np.array([-3, 1, -1, 0, 0, 0])
b = np.array([5, 3, 1])
A = np.array([[1, 1, 1, 0, 0, 0], [1, -2, 0, -1, 0, 0], [2, 1, -1, 0, 1, 0]])

#A[column,row]

def optimal(c):
    z = np.amax(c)
    if z < 0:
        return True
    else:
        return False


def findPivotRow(c, b):
    qi = np.zeros_like(b)
    for l in range(np.size(b)):
        if c[l] != 0:
            qi[l] = b[l] / c[l]
    row = np.argmin(i for i in qi if i > 0)
    print('row', row)
    return row


def findpivotColumn(c):
    column = np.argmax(c)
    print('column', column)
    return column


def makeTableau(c, b, A):
    row = findPivotRow(c, b)
    column = findpivotColumn(c)
    A_new = np.zeros_like(A)
    c_new = np.zeros_like(c)
    print('Pivot', A[column, row])
    # Übertragen der Normalisierten Pivot Zeile
    for i in range(np.size(b)):
        A_new[row, i] = A[row, i] / A[column, row]
    print('aaa',A_new)
    # Füllen des Restlichen Tableaus

    for i in range(np.size(c)):
        for j in range(np.size(b)):
            if j != row:
                A_new[j, i] = A[i, j] - (A[column, i] * A[row, j])
    for i in range(np.size(c)):
        c_new[i] = c[i] - (c[column] * A[row, i])
    print(c_new)
    return A_new , c_new


for i in range(3):
    #while not optimal(c):
        A, c = makeTableau(c, b, A)
        print('-----------------------------------------')

print(A,c)

#print(A)
