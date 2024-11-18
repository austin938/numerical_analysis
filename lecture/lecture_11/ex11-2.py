import numpy as np
import sys
import pathlib

# Get the path to the current script (main.py)
current_script_path = pathlib.Path(__file__).resolve()
project_dir = current_script_path.parents[1]
package_dir_1 = project_dir / 'lecture_10'
sys.path.append(str(package_dir_1))
from solver_10 import rk2

def func(yin: list, t: float) -> np.ndarray:
    N = np.size(yin)
    k = np.zeros(N)

    k[0] = yin[1] # v_y, solve for y
    k[1] = 6*t # a_y, solve for v_y

    return k

h = 0.01
t = 0.0
tend = 1.0

try_y2 = -1.0

yin = [1.0, try_y2]

while t < tend:
    if (t+h) > tend:
        h = tend - t

    y = rk2(yin, t, h, func)
    t += h

    print(f"t={t:e}, y={y[0]:e}")

print(f'y1(1) = {y[0]:e}')
print("The desire value is 1.")