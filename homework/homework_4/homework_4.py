import scipy.linalg as la
import numpy as np
import time
'''
A.shape = (n, n)
solve Ax = b
solve.banded((l, u), ab, b)
where l is the number of diagonals(non zero entry) below than main diagonal,
u is the number of diagonals(non zero entry) above than main diagonal,
ab has the shape of (l+u+1, n) and contains the diagonals of the matrix A.
'''

n = 100
A = np.zeros((n, n))    
for i in range(n):
    # Main diagonal
    if i > 0 and i < n-2:
        A[i,i]=6
    else:
        A[0,0]=9
        A[-1,-1]=1
        A[-2,-2]=5
    # first off diagonal
    if i < n-2: 
        A[i,i+1]=-4 
        A[i+1,i]=-4 
    else:
        A[-1,-2]=-2
        A[-2,-1]=-2
    # second off diagonal
    if i < n-2:
        A[i,i+2]=1
        A[i+2,i]=1

b = np.ones((n, 1))

ab = np.zeros((5, n))
for j in range(n):
    # upper second off diagonal
    if j > 1:
        ab[0,j] = 1
    # upper first off diagonal
    if j > 0 and j < n-1:
        ab[1,j] = -4
    else:
        ab[1,-1] = -2
    # main diagonal
    if j > 0 and j < n-2:
        ab[2,j] = 6
    else:
        ab[2,0] = 9
        ab[2,-1] = 1
        ab[2,-2] = 5
    # lower first off diagonal
    if j < n-1:
        ab[3,j] = -4
    else:
        ab[3,-2] = -2
    # lower second off diagonal
    if j < n-2:
        ab[4,j] = 1


if __name__ == "__main__":
    start_time_1 = time.perf_counter()
    lu, piv = la.lu_factor(A)
    x_1 = la.lu_solve((lu, piv), b)
    end_time_1 = time.perf_counter()
    execution_time_1 = end_time_1 - start_time_1
    # print(f'Solution obtained by method 1 is:\n{x_1}\n it takes {execution_time_1}s')

    start_time_2 = time.perf_counter()
    x_2 = la.solve_banded((2,2), ab, b)
    end_time_2 = time.perf_counter()
    execution_time_2 = end_time_2 - start_time_2
    # print(f'Solution obtained by method 2 is:\n{x_2}\n it takes {execution_time_2}s')

    cond_number = np.linalg.cond(A)
    print("Condition number of A:", cond_number)