import numpy as np
from solver_7 import midpoint, trapezoid_rule, simpson_rule

path = r"C:\Users\austi\OneDrive - NTHU\NTHU\physics\computer\numerical\lecture\lecture_7\data_1\\"


# True answer
pi = np.pi

# Initial parameters
a = -1.0
b = 1.0
N = 10000

A_1 = midpoint(a, b, N)
A_1 = 2*A_1
error_1 = abs(A_1-pi)/pi
with open(path + 'midpoint_1.txt', 'w') as file1:
    file1.write("# Midpoint rule \n")
    file1.write("# N, error, A \n")
    file1.write(f"{N}, {error_1}, {A_1} \n")

A_2 = trapezoid_rule(a, b, N)
A_2 = 2*A_2
error_2 = abs(A_2-pi)/pi
with open(path + 'trapezoid_1.txt', 'w') as file2:
    file2.write("# Trapezoid rule \n")
    file2.write("# N, error, A \n")
    file2.write(f"{N}, {error_2}, {A_2} \n")

A_3 = simpson_rule(a, b, N)
A_3 = 2*A_3
error_3 = abs(A_3-pi)/pi
with open(path + 'simpson_1.txt', 'w') as file3:
    file3.write("# Simpson rule \n")
    file3.write("# N, error, A \n")
    file3.write(f"{N}, {error_3}, {A_3} \n")