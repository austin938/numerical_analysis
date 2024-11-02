import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sci


def function(x):
    return 0.5 - x*np.exp(-x**2)

# define multi input using numpy array
def function_1(x: np.ndarray) -> float:
    return 0.5*x[0]**2 + 2.5*x[1]**2

def jac_1(x: np.ndarray) -> np.ndarray:
    return np.array([x[0], 5*x[1]])

# y > x
def golden_section_search(a, b):
    golden_ratio = (1 + np.sqrt(5)) / 2
    x_0 = b - ((b - a) / golden_ratio)
    x_1 = a + ((b - a) / golden_ratio)
    f_0 = function(x_0)
    f_1 = function(x_1)
    if function(x_0) > function(x_1):
        a = x_0
        x_0 = x_1
        f_0 = f_1
        f_1 = function(a + ((b - a) / golden_ratio))

    else:
        b = x_1
        x_1 = x_0
        f_1 = f_0
        f_0 = function(b - ((b - a) / golden_ratio))
    err = abs(b - a)
    return a, b, function(a), function(b), err

def successive_parabolic_interpolation(x_0, x_1, x_2):
    arr = np.array([x_0, x_1, x_2])
    sorted_array = np.sort(arr) # since cubic spline requires sorted array
    domain = np.linspace(arr.min(), arr.max(), 100)
    func_array = function(sorted_array)
    cubicspline = sci.CubicSpline(sorted_array, func_array)
    cubic = cubicspline(domain)
    min_index = np.argmin(cubic)
    x_0 = arr[1]
    x_1 = arr[2]
    x_2 = domain[min_index]
    f2 = function(x_2)
    err = abs(x_2 - x_1)
    return x_0, x_1, x_2, f2, err

def newton(x):
    x = x - (-1 + 2*x**2) / (6*x - 4*x**3)
    err = abs(np.exp(-x**2)*(-1 + 2*x**2))
    return x, function(x), err

    

if __name__ == "__main__":
    t = np.linspace(-2, 2, 1000)
    plt.plot(t, function(t))
    plt.show()