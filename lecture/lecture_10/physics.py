import numpy as np
from scipy.constants import g
from solver_10 import euler, rk2, rk4


def update(time: float, dt: float, x0: float, y0: float, vx0: float, vy0: float, method: str) -> tuple:
    """
    Update the position and velocity of an object using the specified numerical method.
    Parameters:
    time (float): The current time.
    dt (float): The time step for the update.
    x0 (float): The initial x position.
    y0 (float): The initial y position.
    vx0 (float): The initial velocity in the x direction.
    vy0 (float): The initial velocity in the y direction.
    method (str): The numerical method to use for the update ('euler', 'rk2', 'rk4').
    Returns:
    tuple: A tuple containing the updated x position, y position, x velocity, and y velocity.
    """
    # collect all physical quantities compute in same way into a list
    yin = [x0, y0, vx0, vy0]
    N = np.size(yin)
    
    if method == 'euler':
        yout = euler(yin, time, dt, func)
    elif method == 'rk2':
        yout = rk2(yin, time, dt, func)
    elif method == 'rk4':
        yout = rk4(yin, time, dt, func)
    else:
        raise SystemExit("Error: method "+method+" is not supported!")
    
    return yout[0], yout[1], yout[2], yout[3]


def func(yin: list, time: float) -> np.ndarray:
    
    # time is not used here since dydt is constant in the angry bird problem
    # but we still keep it here for general purposes
    N = np.size(yin)
    # dy/dt = f(y,t)
    k = np.zeros(N) # f(y,t)
    
    k[0] = yin[2] # vx
    k[1] = yin[3] # vy
    k[2] = 0 # ax
    k[3] = -g # ay
    
    return k

