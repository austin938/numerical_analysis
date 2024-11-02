import numpy as np
from linalg import mat_print, solve_lower_triangular_matrix, solve_upper_triangular_matrix

lower = np.array(
    [[-1.0, 0.0, 0.0],
    [-6.0, -4.0, 0.0],
    [1.0, 2.0, 2.0]]
)
upper = np.array(
    [[1.0, 2.0, 2.0],
    [0.0, -4.0, -6.0],
    [0.0, 0.0, -1.0]]
)
b_lower = np.array(
    [
        [1.0],
        [-6.0],
        [3.0]
    ]
)
b_upper = np.array(
    [
        [3.0],
        [-6.0],
        [1.0]
    ]
)

x_lower = solve_lower_triangular_matrix(lower, b_lower)
x_upper = solve_upper_triangular_matrix(upper, b_upper)

mat_print("Lower triangular matrix", lower)
print(f"solution x = \n {x_lower}")
mat_print("Upper triangular matrix", upper)
print(f"solution x = \n {x_upper}")