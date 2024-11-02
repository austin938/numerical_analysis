import numpy as np

def function_1(x):
    return np.sqrt(1-x**2)

# Midpoint rule
def midpoint(a, b, N):
    Area = 0.0
    dx = (b-a)/N
    x = np.linspace(a, b, N, endpoint=True)
    for i in range(N):
        Area += dx*function_1((x[i]+x[i+1])/2)
    return Area

def trapezoid_rule(a, b, N):
    Area = 0.0
    dx = (b-a)/N
    x = np.linspace(a, b, N, endpoint=True)
    for i in range(N):
        Area += dx*(function_1(x[i])+function_1(x[i+1]))/2
    return Area

def simpson_rule(a, b, N):
    Area = 0.0
    dx = (b-a)/N
    x = np.linspace(a, b, N, endpoint=True)
    for i in range(N):
        Area += (dx/6)*(function_1(x[i])+4*function_1((x[i]+x[i+1])/2)+function_1(x[i+1]))
    return Area

if __name__ == "__main__":
    x = 1
    print(function_1(x))