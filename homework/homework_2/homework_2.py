import matplotlib.pyplot as plt
import numpy as np
import scipy as sci

# Domain [1, 5]
time = np.linspace(1, 5, 1000)
a = np.array([[1, 1, 1, 1, 1], 
            [1, 2, 4, 8, 16], 
            [1, 3, 9, 27, 81], 
            [1, 4, 16, 64, 256], 
            [1, 5, 25, 125, 625]])
b = np.array([1, 1, 2, 6, 24])
# data points to interpolate
data_t = np.array([1, 2, 3, 4, 5])
data_y = np.array([1, 1, 2, 6, 24])

# Solving equation a*x = b
x = np.linalg.solve(a, b)
# Polynomial interpolation
y = x[0] + x[1]*time + x[2]*time**2 + x[3]*time**3 + x[4]*time**4
# y = 9 -16.58333*time + 11.625*time**2 - 3.416667*time**3 + 0.375*time**4

# # Cubic spline interpolation
cubic_spline = sci.interpolate.CubicSpline(data_t, data_y)

plt.figure(figsize=(10, 5), layout='constrained')
plt.plot(time, y, linestyle='-.', linewidth=1, label='f(t)')
plt.plot(time, sci.special.gamma(time), linestyle='-', linewidth=1, animated=False, alpha=1, label='gamma(t)')
plt.plot(time, cubic_spline(time), linestyle='-', linewidth=1, label='cubic spline', color='r')
plt.title('interpolation')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid('True')
plt.legend(loc='best')
plt.show()