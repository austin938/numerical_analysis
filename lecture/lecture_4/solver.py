import numpy as np

def function(x: float, function_type: str) -> float:
    """
    function_1: x^2 - 4sin(x)
    function_2: x^3 + 1.5x^2 - 5.75x + 4.37
    """
    if function_type == "function_1":
        return x**2 -4*np.sin(x)
    elif function_type == "function_2":
        return x**3 + 1.5*x**2 - 5.75*x + 4.37
    else:
        return "Invalid function"
    
def derivative(x: float, function_type: str) -> float:
    """
    derivative_1: 2x - 4cos(x)
    derivative_2: 3x^2 + 3x - 5.75
    """
    if function_type == "function_1":
        return 2*x - 4*np.cos(x)
    elif function_type == "function_2":
        return 3*x**2 + 3*x - 5.75

def bisection(a: float, b: float, function_type: str) -> tuple:
    xs = (a+b)/2
    if function(a, function_type)*function(xs, function_type) < 0:
        b = xs
    else:
        a = xs
    err = abs(function(xs, function_type))
    return a, b, xs, err

def newton(xs, function_type):
    xs = xs - function(xs, function_type)/derivative(xs, function_type) # derivative of function_2
    err = abs(function(xs, function_type))
    return xs, err

def secant(x0, x1, function_type):
    xs = x1 - function(x1, function_type)*(x1-x0)/(function(x1, function_type)-function(x0, function_type))
    x0 = x1
    x1 = xs
    err = abs(function(xs, function_type))
    return x0, x1, xs, err

def error_ratio(solution, r):
    errors = abs(solution - 1.93375) # 1.93375 is the approximate solution, since I can't find analytical solution
    return np.array(errors[1:]/errors[:-1]**r)

if __name__ == "__main__":
    print("Hello, you are in solver.py")