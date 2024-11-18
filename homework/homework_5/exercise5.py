import scipy.linalg as la
import matplotlib.pyplot as plt
import numpy as np
'''
n discrete points, n-2 unknowns to solve
'''
def analytical_solution(t):
    return t**3 - t + 1

y0, yN_1 = 1.0, 1.0
a, b = 0.0, 1.0
h = 0.05
n = int((b - a) / h) + 1
t = np.linspace(0, 1, n)


A = np.zeros((n-2, n-2)) 
for i in range(n-2):
    # Main diagonal
    A[i,i]=-2
    # first off diagonal
    if i < n-3:
        A[i,i+1]=1
        A[i+1,i]=1


b = np.zeros((n-2, 1))
for i in range(1, n-1):
    if i == 1:
        b[-i] = 6*h**2*t[i] - y0
    elif i == n-2:
        b[-i] = 6*h**2*t[i] - yN_1
    else:
        b[-i] = 6*h**2*t[i]


ab = np.zeros((3, n-2))
for j in range(n-2):
    # upper first off diagonal
    if j > 0:
        ab[0,j] = 1
    # main diagonal
    ab[1,j] = -2
    # lower first off diagonal
    if j < n-3:
        ab[2,j] = 1


y = la.solve_banded((1,1), ab, b)
y_sort = y[-1::-1] # reverse the order of y
y_sort = np.insert(y_sort, 0, y0) # insert y0 at the beginning
y_sort = np.append(y_sort, yN_1) # append yN_1 at the end


plt.figure(figsize=(8, 6))
plt.plot(t, y_sort, 'o-', label='y(x)')
plt.plot(t, analytical_solution(t), label='analytical', alpha=0.7)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(loc='best')
plt.grid(True)
plt.show()

    