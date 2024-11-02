# Method 2
import math
import numpy as np
import matplotlib.pyplot as plt

N = 100 # terms to add up
x = 1.0 # input x value

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

approx_exp_method_1 = exp_taylor_series_method_1(x, N)
approx_exp_method_2 = exp_taylor_series_method_2(x, N)
exact_exp = np.exp(-x)
# Create a list of N for plotting
list_of_N = [i for i in range(1, N+1)]



# Relative error in Log scale
relative_error_1 = abs(approx_exp_method_1 - exact_exp) / exact_exp
relative_error_2 = abs(approx_exp_method_2 - exact_exp) / exact_exp
log_relative_error_1 = np.log10(relative_error_1)
log_relative_error_2 = np.log10(relative_error_2)

plt.figure(figsize=(8, 6))
plt.plot(list_of_N, log_relative_error_1, label='Method 1', color='red', linestyle='-')
plt.plot(list_of_N, log_relative_error_2, label='Method 2', color='blue', linestyle='--')
plt.xlabel('Number of terms (N)')
plt.ylabel(f'{r"$\log_{10}(abs(relative\ error))$"}')
plt.title(f'Differnet methods of calculating the exponential function at {r"$x = 1.0$"}')
plt.grid(True)
plt.legend()
plt.show()


