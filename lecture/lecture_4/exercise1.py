import numpy as np
import matplotlib.pyplot as plt
from solver import bisection, newton, secant, error_ratio

"""
I can only execute one method at a time, so I will comment out the other two methods.
this is because the initial values are shared between the methods.
This file is for function 1.
"""

path = r"C:\Users\austi\OneDrive - NTHU\NTHU\physics\computer\numerical\lecture\lecture_4\data_1\\"

# parameters
nmax = 50
eps = 1.e-6
err = 1.e99
N = 0

# Bisection's initial guess
a = 1.0
b = 3.0

# Newton's initial guess
xs = 3

# Secant's initial guess
x0 = 1.0
x1 = 3.0

# Bisection method
# with open(path + 'bisection_1.txt', 'w') as file1:
#     file1.write("# N, solution, error \n")
#     while(err > eps):
#         a, b, xs, err = bisection(a, b, "function_1")
#         N += 1
#         file1.write(f"{N}, {xs}, {err} \n")

#         if N > nmax:
#             print("The problem is not converged within", nmax)
#             break

# Newton's method
# with open(path + 'newton_1.txt', 'w') as file2:
#     file2.write("# N, solution, error \n")
#     while(err > eps):
#         xs, err = newton(xs, "function_1")
#         N += 1
#         file2.write(f"{N}, {xs}, {err} \n")

#         if N > nmax:
#             print("The problem is not converged within", nmax)
#             break

# Secant method
# with open(path + 'secant_1.txt', 'w') as file3:
#     file3.write("# N, solution, error \n")
#     while(err > eps):
#         x0, x1, xs, err = secant(x0, x1, "function_1")
#         N += 1
#         file3.write(f"{N}, {xs}, {err} \n")

#         if N > nmax:
#             print("The problem is not converged within", nmax)
#             break

# Exercise 1(a)
# Loading data
bisection_data_1 = np.loadtxt(path + "bisection_1.txt", delimiter=",")
newton_data_1 = np.loadtxt(path + "newton_1.txt", delimiter=",")
secant_data_1 = np.loadtxt(path + "secant_1.txt", delimiter=",")

bisection_n_1=bisection_data_1[0:len(bisection_data_1),0]
bisection_err_1=bisection_data_1[0:len(bisection_data_1),2]
bisection_sol_1=bisection_data_1[0:len(bisection_data_1),1]
bisection_conv_rate=error_ratio(bisection_sol_1,1)

newton_n_1=newton_data_1[0:len(newton_data_1),0]
newton_err_1=newton_data_1[0:len(newton_data_1),2]
newton_sol_1=newton_data_1[0:len(newton_data_1),1]
newton_conv_rate=error_ratio(newton_sol_1,2)

secant_n_1=secant_data_1[0:len(secant_data_1),0]
secant_err_1=secant_data_1[0:len(secant_data_1),2]
secant_sol_1=secant_data_1[0:len(secant_data_1),1]
secant_conv_rate=error_ratio(secant_sol_1,1.5)

# plt.figure(figsize=(10, 5), layout='constrained')
# plt.plot(bisection_n_1,np.log10(bisection_err_1), label="Bisection")
# plt.plot(newton_n_1,np.log10(newton_err_1), label="Newton")
# plt.plot(secant_n_1,np.log10(secant_err_1), label="Secant")
# plt.xlabel('N')
# plt.ylabel(r'$\log_{10}(|error|)$')
# plt.title('Error vs. N')
# plt.grid('True')
# plt.legend(loc='best')
# plt.show()

# Exercise 1(b)
plt.plot(bisection_n_1[:-1],bisection_conv_rate, label="Bisection (r=1)", marker='o', linestyle='--')
plt.plot(newton_n_1[:-1],newton_conv_rate, label="Newton (r=2)", marker='s', linestyle=':')
plt.plot(secant_n_1[:-1],secant_conv_rate, label="Secant (r=1.5)", marker='^', linestyle='--')
plt.xlabel('Iteration (k)')
plt.ylabel(r'$\|e_{k+1}\|/\|e_k\|^r$')
plt.title('Error Ratios vs Iterations for Different Methods')
plt.legend(loc='best')
plt.grid(True)
plt.show()
