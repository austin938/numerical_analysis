import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import secrets

h = np.pi/1000
x = 1
true_ans = -np.cos(x)
def cos(x):
    return np.cos(x)

# eq 1

def central_difference_1(func, x, h):
    return ((func(x+h) - func(x))-(func(x) - func(x-h)))/h**2

numerical_1 = central_difference_1(cos, x, h)
diff_1 = abs(numerical_1 - true_ans)/true_ans
print(f"h={h}, answer={numerical_1}, relative error={diff_1}")

# eq 2

def central_difference_2(func, x, h):
    return (func(x+h) + func(x-h) - 2*func(x))/h**2
numerical_2 = central_difference_2(cos, x, h)
diff_2 = abs(numerical_2 - true_ans)/true_ans
print(f"h={h}, answer={numerical_2}, relative error={diff_2}")



# if I run the same program in different computer with same seed, the output  will be the same.
rng_1 = random.default_rng(seed=1000)
rng_2 = random.default_rng(seed=1937)
N = 1.0e5

x = rng_1.uniform(low=-1, high=1, size=int(N))
y = rng_2.uniform(low=-1, high=1, size=int(N))
func = lambda x, y: x**2 + y**2

inside_x = np.where(func(x, y) < 1)
num_inside = len(inside_x[0])
ratio = num_inside/N
Area = 4*ratio
relative_error = abs(Area - np.pi)/np.pi
print(f"N={N}, Area={Area}, relative error={relative_error}")
# log_N = np.log10(np.)
# log_relative_error = np.log10(relative_error)

# plt.figure()
# plt.plot(log_N, log_relative_error, 'o')
# plt.xlabel("log(N)")
# plt.ylabel("log(relative error)")
# plt.show()

