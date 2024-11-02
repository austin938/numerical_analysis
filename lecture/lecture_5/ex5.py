import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as sci

x = np.linspace(-5, 5, 100) #range of x
data_x = np.array([-2, 0, 1])
data_y = np.array([-27, -1, 0])
yinterp = np.interp(x, data_x, data_y)
cubicspline = sci.CubicSpline(data_x, data_y)

def f(x):
    return -1+5*x-4*x**2

plt.plot(x, f(x), alpha=0.75, label='polynomial')
plt.scatter(data_x, data_y, color='y', label='data')
plt.plot(x, yinterp, linestyle='--', label='interpolation')
plt.plot(x, cubicspline(x), color='r', linestyle=':', label='cubic spline')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(loc='best')
plt.show()

