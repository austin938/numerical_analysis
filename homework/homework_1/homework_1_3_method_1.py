# Method 1
import math
import numpy as np
import matplotlib.pyplot as plt

N = 100 # terms to add up
x = 1.0 # input x value

# I start the series from second term, since first term is n = 0
# which will cause my factorial to be 0
def exp_taylor_series(x, N: int) -> float:
    final_sum = []
    sum = 1.0 # first term of the series
    for n in range(1, N+1):
        sum += (-x)**n / math.factorial(n)
        final_sum.append(sum)
    return final_sum

approx_exp = exp_taylor_series(x, N)
exact_exp = np.exp(-x)
# Create a list of N for plotting
list_of_N = [i for i in range(1, N+1)]


# Plotting comparison with exact and approximated value
plt.figure(figsize=(8, 6))
plt.plot(list_of_N, approx_exp, label=f'Approximation of {r"$\exp(-1)$"}')
# exp(-1) is constant
plt.axhline(y=exact_exp, color='r', linestyle='--', label=f'Exact value of {r"$\exp(-1)$"}')
plt.xlabel('Number of terms (N)')
plt.ylabel(f'{r"$\sum_{n=1}^{N} \frac{(-1)^n}{n!}$"}')
plt.title(f'Approximation of {r"$\exp^(-1)$"} using Taylor Series at {r"$x = 1$"}')
plt.grid(True)
plt.legend()
plt.show()


# Relative error in Log scale
relative_error = abs(approx_exp - exact_exp) / exact_exp
log_relative_error = np.log10(relative_error)
plt.figure(figsize=(8, 6))
plt.plot(list_of_N, log_relative_error, label='Logarithmic Relative Error')
plt.xlabel('Number of terms (N)')
plt.ylabel(f'{r"$\log_{10}(abs(relative\ error))$"}')
plt.title('Relative Error of Approximation of $exp(-1)$ using Taylor Series at $x = 1$')
plt.grid(True)
plt.legend()
plt.show()


# Finding the number of terms that gives the smallest relative error
min_relative_error = np.min(relative_error)
index = np.where(relative_error == min_relative_error)
print(f'At N = {index[0][0] + 1} has the smallest relative error of {min_relative_error}')

'''
The reason why the relative error is smallest at N = 17 is because the roundoff errors, as
N increase the truncation error decrease, while the roundoff error increases. 
'''