import sys
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sci
from multiprocessing import Pool
import time

# Get the path to the current script (main.py)
current_script_path = pathlib.Path(__file__).resolve()
project_dir = current_script_path.parents[2]
package_dir_1 = project_dir / 'lecture' / 'lecture_6'
package_dir_2 = project_dir / 'lecture' / 'lecture_7'
sys.path.append(str(package_dir_1))
sys.path.append(str(package_dir_2))
from solver_6 import function, function_1, jac_1
from solver_7 import midpoint, trapezoid_rule, simpson_rule

# Exwecise 1
# parameters
a = 0.0
b = 2.0
tolerance = 1.e-6

# golden section search
# start_time_1 = time.perf_counter()
# res_gol = sci.minimize_scalar(function, method='golden', bracket=(a, b), tol=tolerance) # *args is addtion arguments for function
# end_time_1 = time.perf_counter()
# execution_time_1 = end_time_1 - start_time_1
# print(f'The minimizer of the function using golden section search is {res_gol.x}')
# print(f'Implement golden section search need {execution_time_1}s')

# # brent section search
# start_time_2 = time.perf_counter()
# res_bre = sci.minimize_scalar(function, method='brent', bracket=(a, b), tol=tolerance)
# end_time_2 = time.perf_counter()
# execution_time_2 = end_time_2 - start_time_2
# print(f'The minimizer of the function using brent section search is {res_bre.x}')
# print(f'Implement brent section search need {execution_time_2}s')

# Exercise 2
x0 = [1.0, 2.0]
# x0 is initial guess, *args is additional arguments for function
# Nelson-Mead method
res_nelder = sci.minimize(function_1, x0, method='Nelder-Mead', tol=tolerance)
print(f'The minimum of function using Nelder-Mead method is {res_nelder.fun}')

# Newton-CG method
res_newton = sci.minimize(function_1, x0, method='Newton-CG', tol=tolerance, jac=jac_1)
print(f'The minimum of function using Newton-CG method is {res_newton.fun}')

# SLSQP method
res_slsqp = sci.minimize(function_1, x0, method='SLSQP', tol=tolerance, jac=jac_1, constraints={
    'type': 'eq', 'fun': lambda x: np.array([x[0] - x[1] - 1]), 'jac': lambda x: np.array([1, -1])
    })
print(f'The minimum of function using SLSQP method is {res_slsqp.fun}')

# Exercise 4
pi = np.pi
right = 1.0
left = -1.0
# Midpoint rule
# def calculate_error_mid(N):
#     A_1 = midpoint(left, right, N)
#     A_1 = 2 * A_1
#     error_1 = abs(A_1 - pi) / pi
#     return error_1
# # Trapezoid rule
# def calculate_error_trap(N):
#     A_2 = trapezoid_rule(left, right, N)
#     A_2 = 2 * A_2
#     error_2 = abs(A_2 - pi) / pi
#     return error_2
# # Simpson rule
# def calculate_error_simp(N):
#     A_3 = simpson_rule(left, right, N)
#     A_3 = 2 * A_3
#     error_3 = abs(A_3 - pi) / pi
#     return error_3

# if __name__ == '__main__':
#     # Parallel processing
#     with Pool() as pool:
#         N_values = np.logspace(1, 7, num=100, base=10, dtype=int)
#         err_1 = pool.map(calculate_error_mid, N_values) # returns a list of errors
#         err_2 = pool.map(calculate_error_trap, N_values)
#         err_3 = pool.map(calculate_error_simp, N_values)
#     log_N_1 = np.log10(N_values)
#     log_err_1 = np.log10(np.array(err_1)) # convert list to array, and do some operations
#     log_err_2 = np.log10(np.array(err_2))
#     log_err_3 = np.log10(np.array(err_3))
#     plt.plot(log_N_1, log_err_1, label='Midpoint rule')
#     plt.plot(log_N_1, log_err_2, label='Trapezoid rule')
#     plt.plot(log_N_1, log_err_3, label='Simpson rule')
#     plt.xlabel(r'$log_{10} N$')
#     plt.ylabel(r'$\log_{10} \varepsilon$')
#     plt.legend(loc='best')
#     plt.grid('True')
#     plt.title('Error vs N')
#     plt.show()

