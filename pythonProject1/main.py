import numpy as np

#c = np.array([-3, 1, -1, 0, 0, 0])
#b = np.array([5.0, 3, 1])
#A = np.array([[1, 1, 1, 0, 0, 0], [1, -2, 0, -1, 0, 0], [2, 1, -1, 0, 1, 0]])
#z = 0

c = np.array([-2, 2, 1, 0, 0, 0])
b = np.array([1, 1, 4.0])
A = np.array([[-1, 2, 1, -1, 1, 0, 0 ], [1, 4, 0, -2, 0, 1, 0], [1, -1, 0, 1, 0, 0, 1]])
z = 0
#A[column,row]

def optimal(c):
    z = np.amax(c)
    if z <= 0:
        return True
    else:
        return False


def findPivotRow(c, b,column):
    q = np.zeros_like(b)
    for i in range(np.size(b)):
        if A[i,column] != 0:
            q[i] = b[i] / A[i, column]
        else:
            q[i] = np.inf
    print('qi', q)
    for i in range(np.size(q)):
        if q[i] < 0:
           q[i] = np.inf
    row = np.argmin(q)
    print('row', row)
    return row


def findpivotColumn(c):
    column = np.argmax(c)
    print('column', column)
    return column


def makeTableau(c, b, A, z):
    column = findpivotColumn(c)
    row = findPivotRow(c, b, column)
    A_new = np.zeros_like(A)
    c_new = np.zeros_like(c)
    b_new = np.zeros_like(b)
    print('Pivot', A[row, column])
    # Übertragen der Normalisierten Pivot Zeile
    for i in range(np.size(c)):
        A_new[row, i] = A[row, i] / A[row,column]
    # Füllen des Restlichen Tableaus

    for i in range(np.size(b)):
        if i != row:
            for j in range(np.size(c)):
                A_new[i, j] = A[i, j] - (A[i, column] * A[row, j])
    for i in range(np.size(c)):
        c_new[i] = c[i] - (c[column] * A[row, i])

    for i in range(np.size(b)):
        if i == row:
            b_new[i] = b[i] / A[row, column]
        else:
            b_new[i] = b[i] - b[row] * A[i, column]

    z = z - b[row] * c[column]

    print('A_new', A_new)
    print('b_new', b_new)
    print('c_new', c_new)
    print('-------------')

    return A_new , c_new, b_new, z



while not optimal(c):
    A, c, b, z = makeTableau(c, b, A, z)
    print('-----------------------------------------')


print(A)
print(c)
print(b)
print(z)

#print(A)
#inspired by Daniel