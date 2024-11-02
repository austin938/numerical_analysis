# Method 3
import math
import numpy as np
import matplotlib.pyplot as plt

# terms to add up
N = 100
# input x value
x_1 = 1.0
x_2 = 10.0
x_3 = 100.0


def exp_taylor_series_method_1(x, N: int) -> float:
    final_sum = []
    sum = 1.0 # first term of the series
    for n in range(1, N+1):
        sum += (-x)**n / math.factorial(n)
        final_sum.append(sum)
    return final_sum

def exp_taylor_series_method_2(x, N: int) -> float:
    final_sum = []
    sum = 1.0 # first term of the series
    factorial = 1.0
    x_term = 1.0
    for n in range(1, N+1):
        factorial *= n # n! = n*(n-1)!
        x_term *= -x # (-x)^n = (-x)^n-1*(-x)
        sum += x_term / factorial
        final_sum.append(sum)
    return final_sum

def exp_taylor_series_method_3(x, N: int) -> float:
    final_sum = []
    sum = 1.0 # first term of the series
    factorial = 1.0
    x_term = 1.0
    for n in range(1, N+1):
        factorial *= n # n! = n*(n-1)!
        x_term *= x # x^n = x^n-1*x
        sum += x_term / factorial
        final_sum.append(sum)
    return 1 / np.array(final_sum)

# Implement the exponential function for x = 1.0
approx_exp_method_1_x1 = exp_taylor_series_method_1(x_1, N)
approx_exp_method_2_x1 = exp_taylor_series_method_2(x_1, N)
approx_exp_method_3_x1 = exp_taylor_series_method_3(x_1, N)
exact_exp_x1 = np.exp(-x_1)
# Create a list of N for plotting
list_of_N = [i for i in range(1, N+1)]

# Relative error in Log scale for x = 1.0
relative_error_1_x1 = abs(approx_exp_method_1_x1 - exact_exp_x1) / exact_exp_x1
relative_error_2_x1 = abs(approx_exp_method_2_x1 - exact_exp_x1) / exact_exp_x1
relative_error_3_x1 = abs(approx_exp_method_3_x1 - exact_exp_x1) / exact_exp_x1
log_relative_error_1_x1 = np.log10(relative_error_1_x1)
log_relative_error_2_x1 = np.log10(relative_error_2_x1)
log_relative_error_3_x1 = np.log10(relative_error_3_x1)

plt.figure(figsize=(8, 6))
plt.plot(list_of_N, log_relative_error_1_x1, label='Method 1', color='red', linestyle='-')
plt.plot(list_of_N, log_relative_error_2_x1, label='Method 2', color='blue', linestyle='--')
plt.plot(list_of_N, log_relative_error_3_x1, label='Method 3', color='green', linestyle='-.')
plt.xlabel('Number of terms (N)')
plt.ylabel(f'{r"$\log_{10}(abs(relative\ error))$"}')
plt.title(f'Differnet methods of calculating the exponential function at {r"$x = 1.0$"}')
plt.grid(True)
plt.legend()
plt.show()


# Implement the exponential function for x = 10.0
approx_exp_method_1_x2 = exp_taylor_series_method_1(x_2, N)
approx_exp_method_2_x2 = exp_taylor_series_method_2(x_2, N)
approx_exp_method_3_x2 = exp_taylor_series_method_3(x_2, N)
exact_exp_x2 = np.exp(-x_2)
# Create a list of N for plotting
list_of_N = [i for i in range(1, N+1)]

# Relative error in Log scale for x = 10.0
relative_error_1_x2 = abs(approx_exp_method_1_x2 - exact_exp_x2) / exact_exp_x2
relative_error_2_x2 = abs(approx_exp_method_2_x2 - exact_exp_x2) / exact_exp_x2
relative_error_3_x2 = abs(approx_exp_method_3_x2 - exact_exp_x2) / exact_exp_x2
log_relative_error_1_x2 = np.log10(relative_error_1_x2)
log_relative_error_2_x2 = np.log10(relative_error_2_x2)
log_relative_error_3_x2 = np.log10(relative_error_3_x2)

plt.figure(figsize=(8, 6))
plt.plot(list_of_N, log_relative_error_1_x2, label='Method 1', color='red', linestyle='-')
plt.plot(list_of_N, log_relative_error_2_x2, label='Method 2', color='blue', linestyle='--')
plt.plot(list_of_N, log_relative_error_3_x2, label='Method 3', color='green', linestyle='-.')
plt.xlabel('Number of terms (N)')
plt.ylabel(f'{r"$\log_{10}(abs(relative\ error))$"}')
plt.title(f'Differnet methods of calculating the exponential function at {r"$x = 10.0$"}')
plt.grid(True)
plt.legend()
plt.show()


# Implement the exponential function for x = 100.0
approx_exp_method_1_x3 = exp_taylor_series_method_1(x_3, N)
approx_exp_method_2_x3 = exp_taylor_series_method_2(x_3, N)
approx_exp_method_3_x3 = exp_taylor_series_method_3(x_3, N)
exact_exp_x3 = np.exp(-x_3)
# Create a list of N for plotting
list_of_N = [i for i in range(1, N+1)]

# Relative error in Log scale for x = 100.0
relative_error_1_x3 = abs(approx_exp_method_1_x3 - exact_exp_x3) / exact_exp_x3
relative_error_2_x3 = abs(approx_exp_method_2_x3 - exact_exp_x3) / exact_exp_x3
relative_error_3_x3 = abs(approx_exp_method_3_x3 - exact_exp_x3) / exact_exp_x3
log_relative_error_1_x3 = np.log10(relative_error_1_x3)
log_relative_error_2_x3 = np.log10(relative_error_2_x3)
log_relative_error_3_x3 = np.log10(relative_error_3_x3)

plt.figure(figsize=(8, 6))
plt.plot(list_of_N, log_relative_error_1_x3, label='Method 1', color='red', linestyle='-')
plt.plot(list_of_N, log_relative_error_2_x3, label='Method 2', color='blue', linestyle='--')
plt.plot(list_of_N, log_relative_error_3_x3, label='Method 3', color='green', linestyle='-.')
plt.xlabel('Number of terms (N)')
plt.ylabel(f'{r"$\log_{10}(abs(relative\ error))$"}')
plt.title(f'Differnet methods of calculating the exponential function at {r"$x = 100.0$"}')
plt.grid(True)
plt.legend()
plt.show()