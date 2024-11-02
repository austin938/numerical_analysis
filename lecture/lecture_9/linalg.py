import numpy as np

def mat_print(msg, matrix):
    print(msg+'\n')
    nrow, ncol = matrix.shape
    for i in range(nrow):
        outstr=""
        for j in range(ncol):
            outstr += f"{matrix[i,j]:.3f}  "
        outstr += "\n"
        print(outstr)

def solve_lower_triangular_matrix(L, b):
    x = np.zeros((1,b.shape[0]))
    for j in range(L.shape[1]):
        if L[j,j] == 0:
            break
        x[0,j] = b[j] / L[j,j]
        for i in range(j, L.shape[0]):
            b[i] -= L[i,j]*x[0,j]
    return x.T

def solve_upper_triangular_matrix(U, b):
    x = np.zeros((1,b.shape[0]))
    for j in range(b.shape[0]-1, -1, -1):
        if U[j,j] == 0:
            break
        x[0,j] = b[j] / U[j,j]
        for i in range(0, j):
            b[i] -= U[i,j]*x[0,j]
    return x.T
    

if __name__ == "__main__":
    a=np.array(
        [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]
    )
    mat_print("Matrix a", a)