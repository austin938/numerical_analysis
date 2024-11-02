import numpy as np
import matplotlib.pyplot as plt
from solver import bisection, newton, secant

"""
I can only execute one method at a time, so I will comment out the other two methods.
this is because the initial values are shared between the methods.
This file is for function 2.
"""

path = r"C:\Users\austi\OneDrive - NTHU\NTHU\physics\computer\numerical\lecture\lecture_4\data_2\\"

# parameters
nmax = 50
eps = 1.e-6
err = 1.e99
N = 0
# Bisection's initial guess
a = -5.0
b = -2.0

# Newton's initial guess
xs = -2.0

# Secant's initial guess
x0 = -5.0
x1 = -2.0

# Bisection method
# file1 = open(path + 'bisection_2.txt', 'w')
# file1.write("# N solution error \n")
# file1.write("# N, solution, error \n")
# while(err > eps):
#     a, b, xs, err = bisection(a, b, "function_2")
#     N += 1
#     file1.write(f"{N}, {xs}, {err} \n")

#     if N > nmax:
#         print("The problem is not converged within", nmax)
#         break
# file1.close()

# Newton's method
# file2 = open(path + 'newton_2.txt', 'w')
# file2.write("# N solution error \n")
# file2.write("# N, solution, error \n")
# while(err > eps):
#     xs, err = newton(xs, "function_2")
#     N += 1
#     file2.write(f"{N}, {xs}, {err} \n")

#     if N > nmax:
#         print("The problem is not converged within", nmax)
#         break
# file2.close()

# Secant method
# file3 = open(path + 'secant_2.txt', 'w')
# file3.write("# N solution error \n")
# file3.write("# N, solution, error \n")
# while(err > eps):
#     x0, x1, xs, err = secant(x0, x1, "function_2")
#     N += 1
#     file3.write(f"{N}, {xs}, {err} \n")

#     if N > nmax:
#         print("The problem is not converged within", nmax)
#         break
# file3.close()

# Exercise 1(a)
# Loading data & Plotting
bisection_data_2 = np.loadtxt(path + "bisection_2.txt", delimiter=",")
newton_data_2 = np.loadtxt(path + "newton_2.txt", delimiter=",")
secant_data_2 = np.loadtxt(path + "secant_2.txt", delimiter=",")

bisection_n_2=bisection_data_2[0:len(bisection_data_2),0]
bisection_err_2=bisection_data_2[0:len(bisection_data_2),2]

newton_n_2=newton_data_2[0:len(newton_data_2),0]
newton_err_2=newton_data_2[0:len(newton_data_2),2]

secant_n_2=secant_data_2[0:len(secant_data_2),0]
secant_err_2=secant_data_2[0:len(secant_data_2),2]

plt.figure(figsize=(10, 5), layout='constrained')
plt.plot(bisection_n_2,np.log10(bisection_err_2), label="Bisection")
plt.plot(newton_n_2,np.log10(newton_err_2), label="Newton")
plt.plot(secant_n_2,np.log10(secant_err_2), label="Secant")
plt.xlabel('N')
plt.ylabel(r'$\log_{10}(|error|)$')
plt.title('Error vs. N')
plt.legend(loc='best')
plt.grid('True')
plt.show()