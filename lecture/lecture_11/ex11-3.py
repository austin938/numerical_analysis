import numpy as np
import sys
import pathlib

# Get the path to the current script (main.py)
current_script_path = pathlib.Path(__file__).resolve()
project_dir = current_script_path.parents[1]
package_dir_1 = project_dir / 'lecture_10'
sys.path.append(str(package_dir_1))
from solver_10 import rk2

def func(yin: list, time: float) -> np.ndarray:
    N = np.size(yin)
    k = np.zeros(N)

    k[0] = yin[1]
    k[1] = 6*time

    return k

iter_max = 100
tol = 1.0e-8
error = 1.e99
try_y2_min = -1.5
try_y2_max = 2.0
expected_y = 1.0

iter = 0
while error >= tol:
    h = 0.01
    t = 0.0
    tend = 1.0

    try_y2 = (try_y2_min + try_y2_max)/2.0

    yin = [1.0, try_y2]
    
    y = rk2(yin, t, h, func)
    t += h

    error = abs((y[0] - expected_y)/expected_y)

    if y[0] > expected_y:
        try_y2_max = try_y2
    else:
        try_y2_min = try_y2

    iter += 1
    if iter >= iter_max:
        print("Error: Bisection method reached max iterations.")
        break

    print(f"y1(1) = {y[0]:e}, error = {error:e}")