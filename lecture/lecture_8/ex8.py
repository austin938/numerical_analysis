import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import os
import secrets

h = np.pi/1000
x = 1
true_ans = -np.cos(x)
def cos(x):
    return np.cos(x)

# eq 1

def central_difference_1(func, x, h):
    return ((func(x+h) - func(x))-(func(x) - func(x-h)))/h**2

# h1 = np.linspace(10e-10, np.pi/10, 100000, endpoint=True) # start from 10^-10 to pi/10, 100000 points
# numerical_1 = central_difference_1(cos, x, h1)
# log_h1 = np.log(h1)
# diff_1 = abs((numerical_1 - true_ans)/true_ans)
# log_diff_1 = np.log(diff_1)
# min_error_index = np.argmin(log_diff_1) # return the index of the minimum value
# optimal_h = h1[min_error_index]
# print(f"The step size that minimizes the relative error is approximately: {optimal_h}")

# plt.figure(figsize=(10, 5), layout='constrained')
# plt.plot(log_h1, log_diff_1, marker='o', label='central difference')
# plt.xlabel(r"$ln h$")
# plt.ylabel(r"$ln \varepsilon$")
# plt.title("Log-Log Plot of Relative Error vs Step Size")
# plt.legend(loc='best')
# plt.grid('True')

# # Define the directory and filename
directory = 'homework/homework_4/picture'
filename_1 = 'Exercise_1_plot.png'

# # Ensure the directory exists
# os.makedirs(directory, exist_ok=True)

# # Save the plot to the specified directory with the specified filename
# plt.savefig(os.path.join(directory, filename_1))

# plt.show()
# print(f"h={h}, answer={numerical_1}, relative error={log_diff_1}")

# eq 2

def central_difference_2(func, x, h):
    return (func(x+h) + func(x-h) - 2*func(x))/h**2
numerical_2 = central_difference_2(cos, x, h)
# diff_2 = abs(numerical_2 - true_ans)/true_ans
# print(f"h={h}, answer={numerical_2}, relative error={diff_2}")



# If I run the same program in different computer with same seed, the output  will be the same.
rng_1 = random.default_rng(seed=1000)
rng_2 = random.default_rng(seed=1937)
N = np.logspace(2, 7, 1000, base=10, endpoint=True, dtype=int)

Area = []
relative_error = []
for n in N:
    x = rng_1.uniform(low=-1, high=1, size=int(n))
    y = rng_2.uniform(low=-1, high=1, size=int(n))
    func = lambda x, y: x**2 + y**2

    # Monte Carlo integration
    inside_x = np.where(func(x, y) < 1)
    num_inside = len(inside_x[0])
    ratio = num_inside/n
    area = 4*ratio
    Area.append(area)
    relative_error.append(abs((area - np.pi)/np.pi))
    # print(f"N={N}, Area={Area}, relative error={relative_error}")

# print(f"Area={len(Area)}, relative error={len(relative_error)}")
log_N = np.log(N)
log_relative_error = np.log(relative_error)
plt.figure(figsize=(10, 5))
plt.plot(log_N, log_relative_error, label='Monte Carlo Integration')
plt.plot(log_N, -0.5*log_N - 1.5, linestyle='--', label='slope=-0.5')
plt.xlabel(r"$ln N$")
plt.ylabel(r"$ln \varepsilon$")
plt.title("Log-Log Plot of Relative Error vs Number of Points")
plt.legend(loc='best')
plt.grid('True')
filename_2 = 'Exercise_2_plot.png'

# # Save the plot to the specified directory with the specified filename
plt.savefig(os.path.join(directory, filename_2))
plt.show()

