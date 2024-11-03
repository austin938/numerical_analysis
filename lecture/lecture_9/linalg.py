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
        x[0,j] = b[j,0] / L[j,j] # float64
        for i in range(j, L.shape[0]):
            b[i,0] -= L[i,j]*x[0,j]
    return x.T # return x as a column vector(Transpose)

def solve_upper_triangular_matrix(U, b):
    x = np.zeros((1,b.shape[0]))
    for j in range(b.shape[0]-1, -1, -1):
        if U[j,j] == 0:
            break
        x[0,j] = b[j,0] / U[j,j]
        for i in range(0, j):
            b[i,0] -= U[i,j]*x[0,j]
    return x.T

def LU_decomposition(A):
    M = np.zeros(A.shape)
    U = np.zeros(A.shape)
    n = A.shape[0]
    for k in range(n):
        if A[k,k] == 0:
            break
        for i in range(k+1, n):
            M[i,k] = A[i,k]/A[k,k]
        for j in range(k+1, n):
            for i in range(k+1, n):
                A[i,j] -= M[i,k]*A[k,j]
        for j in range(k, n):
            U[k,j] = A[k,j]
    L = M + np.eye(n)
    return L, U

def solve_lu(A, b):
    L, U = LU_decomposition(A)
    y = solve_lower_triangular_matrix(L, b)
    x = solve_upper_triangular_matrix(U, y)
    return x

if __name__ == "__main__":
    A_exercise4_1 = np.array([[1, 2, 2],
                        [4, 6, 8],
                        [4, 8, 10]])

    b_exercise4_1 = np.array([[4],
                            [6],
                            [10]])
    x = solve_lu(A_exercise4_1, b_exercise4_1)                          
    print(x)