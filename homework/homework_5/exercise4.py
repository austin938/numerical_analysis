import sys
import pathlib
# Get the path to the current script (main.py)
current_script_path = pathlib.Path(__file__).resolve()
project_dir = current_script_path.parents[2]
package_dir_1 = project_dir / 'lecture' / 'lecture_10'
sys.path.append(str(package_dir_1))
from solver_10 import rk4
import numpy as np
from scipy.constants import g


v0 = 30.0
dt = 0.01
t_max = 10.0
tol = 1e-5
angle_min = 0.0
angle_max = np.pi/2
bound_x = 50.0 # boundary condition of system y(50) = 0

# behavior of the system
def equation_of_motion(state: list, time: float) -> np.ndarray:
    k = np.zeros_like(state)

    k[0] = state[2] # dx/dt = vx
    k[1] = state[3] # dy/dt = vy
    k[2] = 0.0 # dvx/dt = 0
    k[3] = -g # dvy/dt = -g

    return k


def shoot(angle: float) -> float:
    vx0 = v0 * np.cos(angle)
    vy0 = v0 * np.sin(angle)
    state = np.array([0.0, 0.0, vx0, vy0])
    time = 0.0
    while time < t_max:
        state = rk4(state, time, dt, equation_of_motion)
        time += dt
        if state[1] < 0.0:
            break
    return state[0] # return the x value when y hits the ground


def bisection_method(bound_x, tol, angle_min, angle_max):
    while angle_max - angle_min > tol:
        angle_try = (angle_min + angle_max)/2
        x_try = shoot(angle_try)
        if x_try < bound_x: 
            angle_min = angle_try
        else:
            angle_max = angle_try
    return (angle_min + angle_max)/2

angle = bisection_method(bound_x, tol, angle_min, angle_max)
print(f"Optimal angle: {np.degrees(angle):.2f} degrees")