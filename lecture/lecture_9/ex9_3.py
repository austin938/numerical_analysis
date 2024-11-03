from linalg import *
import numpy as np

A_example = np.array([[2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])

A_exercise4_1 = np.array([[1, 2, 2],
                        [4, 6, 8],
                        [4, 8, 10]])

b_exercise4_1 = np.array([[4],
                          [6],
                          [10]])

L_1, U_1 = LU_decomposition(A_example)
print(f'This is example Lower matrix:\n{L_1}')
print(f'This is example Upper matrix:\n{U_1}')

L_2, U_2 = LU_decomposition(A_exercise4_1)
print(f'This is exercise 4 Lower matrix:\n{L_2}')
print(f'This is exercise 4 Upper matrix:\n{U_2}')

x = solve_lu(A_exercise4_1, b_exercise4_1)                          
print(f'Solution of exercise 4 obtained by LU decomposition:\n{x}')